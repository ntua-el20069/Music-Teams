from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort
from flask_httpauth import HTTPBasicAuth
import mysql.connector
#import psycopg2 

from __init__ import get_db

'''Functions to select/insert/update/delete from the Database'''

def get_song_by_id(song_id: int) -> tuple:
    db = get_db()
    cursor = db.cursor()
    
    sql = f"select title, lyrics, chords  from  song where id={song_id}"
    cursor.execute(sql)
    title, lyrics, chords = cursor.fetchall()[0]
    #title, lyrics, chords = [title.encode('utf-8'), lyrics.encode('utf-8'), chords.encode('utf-8')]
    
    sql = f"select composer from wrotemusic where song_id={song_id}"
    cursor.execute(sql)
    composers_list = [x[0] for x in cursor.fetchall()]
    composers = ', '.join(composers_list)
    
    sql = f"select lyricist from wrotelyrics where song_id={song_id}"
    cursor.execute(sql)
    lyricists_list = [x[0] for x in cursor.fetchall()]
    lyricists = ', '.join(lyricists_list)
    
    #print(title) # for debugging
    
    cursor.close()
    return (title, lyrics, chords, composers, lyricists)

def get_id_by_title(song_title: str) -> int:
    db = get_db()
    cursor = db.cursor()
    sql = f'''select id  from  song where title="{song_title}"'''
    cursor.execute(sql)
    id = cursor.fetchall()[0][0]
    cursor.close()
    return id


def unique_song(title, lyricists: list):
    # check that there is not any song with the same (title and lyricist)
    # (for each lyricist check that there is no entry in [WroteLyrics join Song] that refers to the same title)
    db = get_db()
    cursor = db.cursor()
    for lyricist in lyricists:
        sql = f"""select *  from song S join wrotelyrics W on S.id = W.song_id where title="{title}" and lyricist="{lyricist}" """
        cursor.execute(sql)
        if cursor.fetchall(): return False
    cursor.close()
    return True
    

def insert_song(title, composers: str, lyricists: str, lyrics) -> tuple:
    '''function for song insertion in DB-> returns a message'''
    db = get_db()
    # split composers and lyricists 
    composers_list = [x.strip() for x in composers.split(',')]
    lyricists_list = [x.strip() for x in lyricists.split(',')]
    
    if not unique_song(title, lyricists_list):
        return (f'There is already a song with title: {title} and lyricist some of them: {lyricists}', 0)

    # if not exists -> insert into Database tables: Song , WroteMusic , WroteLyrics
    # insert also into Composer, Lyricist (if not inserted already)
    cursor = db.cursor()
    for composer in composers_list:
        try:
            sql = f"""insert into composer values ("{composer}")"""
            cursor.execute(sql)
            db.commit()
        except:
            print(f"composer: {composer} was already in Database")
    for lyricist in lyricists_list:
        try:
            sql = f"""insert into lyricist values ("{lyricist}")"""
            cursor.execute(sql)
            db.commit()
        except:
            print(f"lyricist: {lyricist} was already in Database")
    try:
        sql = f"""insert into song(title, lyrics) values ("{title}", "{lyrics}")"""
        cursor.execute(sql)
        db.commit()
        sql = f"select max(id) from song"
        cursor.execute(sql)
        id = cursor.fetchall()[0][0]

        for composer in composers_list:
            sql = f"""insert into wrotemusic values ("{composer}","{id}")"""
            cursor.execute(sql)
            db.commit()
        for lyricist in lyricists_list:
            sql = f"""insert into wrotelyrics values ("{lyricist}","{id}")"""
            cursor.execute(sql)
            db.commit()
    except:
        return ("Song Insertion failed due to an error in tables, Song, WroteMusic or WroteLyrics", id)
    return ('', id)
            

def update_song(song_id, title, composers: str, lyricists: str, lyrics) -> str:
    '''used for update song in DB (title, composer, lyricist, lyrics) -> returns a message'''
    db = get_db()
    # split composers and lyricists
    composers_list = [x.strip() for x in composers.split(',')]
    lyricists_list = [x.strip() for x in lyricists.split(',')]
    
    old_title, _, _, _ , old_lyricists = get_song_by_id(song_id)
    if old_title != title or old_lyricists != lyricists:    # if title or lyricists changed check...
        if not unique_song(title, lyricists_list):
            return f'There is already a song with title: {title} and lyricist some of them: {lyricists}'
    
    # insert also into Composer, Lyricist (if not inserted already)
    cursor = db.cursor()
    for composer in composers_list:
        try:
            sql = f"""insert into composer values ("{composer}")"""
            cursor.execute(sql)
            db.commit()
        except:
            print(f"composer: {composer} was already in Database")
    for lyricist in lyricists_list:
        try:
            sql = f"""insert into lyricist values ("{lyricist}")"""
            cursor.execute(sql)
            db.commit()
        except:
            print(f"lyricist: {lyricist} was already in Database")
    try:
        # if not exists -> update Database tables: Song
        sql = f"""update song set title="{title}", lyrics="{lyrics}" where id={song_id}"""
        cursor.execute(sql)
        db.commit()
        # delete from WroteMusic , WroteLyrics the tuples that refer to this song_id
        sql = f"""delete from wrotemusic where song_id={song_id}"""
        cursor.execute(sql)
        db.commit()
        sql = f"""delete from wrotelyrics where song_id={song_id}"""
        cursor.execute(sql)
        db.commit()
        # # insert the new composers, lyricists in WroteMusic , WroteLyrics
        for composer in composers_list:
            sql = f"""insert into wrotemusic values ("{composer}","{song_id}")"""
            cursor.execute(sql)
            db.commit()
        for lyricist in lyricists_list:
            sql = f"""insert into wrotelyrics values ("{lyricist}","{song_id}")"""
            cursor.execute(sql)
            db.commit()
    except:
        return "Song Insertion failed due to an error in tables, Song, WroteMusic or WroteLyrics"
    return ''

def update_lyrics_chords(song_id, lyrics, chords):
    '''used for insert/update chords in DB (and maybe lyrics) to a song'''
    db = get_db()
    cursor = db.cursor()
    try:
        sql = f"""update song set lyrics="{lyrics}", chords="{chords}" where id="{song_id}" """
        cursor.execute(sql)
        db.commit()
    except:
        print("Error in lyrics and chords update")
    

def update_chords(song_id, chords):
    '''used for permanent transporto in DB'''
    db = get_db()
    cursor = db.cursor()
    try:
        sql = f"""update song set chords="{chords}" where id="{song_id}" """
        cursor.execute(sql)
        db.commit()
    except:
        print("Error in chords update")