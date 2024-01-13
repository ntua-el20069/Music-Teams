from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector
from web_scrape import take_from_greeklyrics
#import psycopg2 

from help_routes import *
from __init__ import get_db, list_url
from all import *


def home():
    db = get_db()
    cursor = db.cursor()
    sql = "select title from song"
    cursor.execute(sql)
    songs = [x[0] for x in cursor.fetchall()]
    ids = []
    selected = ''
    if request.method == 'POST':
        selected = request.form.get('find') 
        print(selected)
        sql = f"""select id from song where title="{selected}" """
        cursor.execute(sql)
        ids = [x[0] for x in cursor.fetchall()]
        print(ids)
    return render_template('home.html', songs=songs, ids=ids, selected=selected)

def home_json():
    db = get_db()
    cursor = db.cursor()
    sql = "SELECT title FROM song"
    cursor.execute(sql)
    songs = [x[0] for x in cursor.fetchall()]
    ids = []
    selected = ''

    if request.method == 'POST':
        request_data = request.get_json()

        if request_data is None or 'find' not in request_data:
            return jsonify({"error": "Invalid JSON format or missing 'find' key"}), 400  # Bad Request

        selected = request_data.get('find')
        print(selected)
        sql = f"""SELECT id FROM song WHERE title="{selected}" """
        cursor.execute(sql)
        ids = [x[0] for x in cursor.fetchall()]
        print(ids)
        if not ids:
            return jsonify({"error": f"No song found for title: '{selected}'"}), 404  # Not Found

    response_data = {
        "songs": songs,
        "ids": ids,
        "selected": selected
    }
    
    response = jsonify(response_data)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 200  # OK


def add_lyrics(song_id = '', update = False):
    
    if request.method == 'GET':
        if update == True:
            title, lyrics, _, composers, lyricists = get_song_by_id(song_id)
        else:
            title = ""
            composers = ""
            lyricists = ""
            lyrics = ''
        return render_template('add-lyrics.html', title = title, composers=composers, lyricists=lyricists, lyrics=lyrics, all_composers = all_composers(), all_lyricists = all_lyricists(), songs = all_songs())
    elif request.method == 'POST':
        title = request.form.get('title')
        composers = request.form.get('composer')
        lyricists = request.form.get('lyricist')
        lyrics = request.form.get('lyrics')
        search_title = title
        button_info = request.form.get('button-info')
        if button_info=='find-lyrics': # Web Scraping
            title, composers, lyricists, lyrics = take_from_greeklyrics(title)
            if not title: 
                msg = lyrics
                return render_template('add-lyrics.html', title = search_title, composers='', lyricists='', lyrics='', all_composers = all_composers(), all_lyricists = all_lyricists(), songs = all_songs()) \
                     + f"<p style='color: red;'>The song: {search_title} cannot be found due to {msg}</p>"   # returns the error message
            return render_template('add-lyrics.html', title = title, composers=composers, lyricists=lyricists, lyrics=lyrics, all_composers = all_composers(), all_lyricists = all_lyricists(), songs = all_songs())
        
        #print("I got the submitted info from the form")
        massive = ''
        if button_info=='massive-submit':
            massive = render_template('add-lyrics.html', title = search_title, composers='', lyricists='', lyrics='', all_composers = all_composers(), all_lyricists = all_lyricists(), songs = all_songs()) 
        if update:
            message = update_song(song_id, title, composers, lyricists, lyrics)
            if message: return f"<h1>{message}</h1>"
            return massive + f"Successful Updation! <br> <a href='/{song_id}/update-chords'>Update chords</a> <br> <a href='/'>Home</a> <br>"
            
        message, song_id = insert_song(title, composers, lyricists, lyrics)
        if message: return f"<h1>{message}</h1>"
        return massive + f"Successful Insertion!  <br> <a href='/{song_id}/add-chords'>Add chords</a> <br> <a href='/'>Home</a> <br>"
    else:
        pass

def add_lyrics_json(song_id='', update=False):
    if request.method == 'GET':
        if update:
            title, lyrics, _, composers, lyricists = get_song_by_id(song_id)
        else:
            title = ""
            composers = ""
            lyricists = ""
            lyrics = ''
        return jsonify({
            "title": title,
            "composers": composers,
            "lyricists": lyricists,
            "lyrics": lyrics,
            "all_composers": all_composers(),
            "all_lyricists": all_lyricists(),
            "songs": all_songs()
        })

    elif request.method == 'POST':
        request_data = request.get_json()

        if request_data is None:
            return jsonify({"error": "Invalid JSON format in the request"}), 400  # Bad Request

        title = request_data.get('title')
        composers = request_data.get('composer')
        lyricists = request_data.get('lyricist')
        lyrics = request_data.get('lyrics')
        search_title = title
        button_info = request_data.get('button-info')

        if button_info == 'find-lyrics':
            title, composers, lyricists, lyrics = take_from_greeklyrics(title)
            if not title:
                msg = lyrics
                return jsonify({"error": f"The song: {search_title} cannot be found due to {msg}"}), 404  # Not Found
            return jsonify({
                "title": title,
                "composers": composers,
                "lyricists": lyricists,
                "lyrics": lyrics,
                "all_composers": all_composers(),
                "all_lyricists": all_lyricists(),
                "songs": all_songs()
            }), 200  # OK

        massive = ''
        if button_info == 'massive-submit':
            massive = {
                "title": search_title,
                "composers": '',
                "lyricists": '',
                "lyrics": '',
                "all_composers": all_composers(),
                "all_lyricists": all_lyricists(),
                "songs": all_songs()
            }

        if update:
            message = update_song(song_id, title, composers, lyricists, lyrics)
            if message:
                return jsonify({"message": message}), 400  # Bad Request
            return jsonify({
                "message": "Successful Updation!",
                "links": {
                    "update_chords": f"/{song_id}/update-chords",
                    "home": "/"
                }
            }), 200  # OK

        message, song_id = insert_song(title, composers, lyricists, lyrics)
        if message:
            return jsonify({"message": message, song_id: -1}), 400  # Bad Request
        return jsonify({
            "message": "Successful Insertion!",
            "links": {
                "add_chords": f"/{song_id}/add-chords",
                "home": "/"
                
            },
            "song_id": song_id
        }), 201  # Created

    else:
        return jsonify({"error": "Invalid request method"}), 405  # Method Not Allowed



def add_chords(song_id, update = False):
    
    title, lyrics, chords, composers, lyricists = get_song_by_id(song_id)
    if request.method == 'GET':
        if chords=='' or update==False or chords is None:
            chords = '\n'.join(len(lyrics.split('\n')) * [''])
        elif len(chords.split('\n')) != len(lyrics.split('\n')):    # if rows of lyrics != rows of chords
            k = len(lyrics.split('\n')) - len(chords.split('\n'))
            chords += k*'\n'                                       # make rows the same
        chords_list = [ x + (100 - len(x)) * ' '  for x in chords.split('\n')]  # because 100 is max input size
        lyrics_list = lyrics.split('\n')
        return render_template('add-chords.html', title=title, composers=composers, lyricists=lyricists, lyrics_list=lyrics_list, chords_list=chords_list, song_id=song_id, i=0, zip=zip) 
    elif request.method == 'POST':
        lines = len(lyrics.split('\n'))
        lyrics = []
        chords = []
        for i in range(lines):
            lyrics_line = request.form.get(f'lyricsLine-{i+1}')
            lyrics_line = lyrics_line if lyrics_line else ''
            chords_line = request.form.get(f'chordsLine-{i+1}')
            chords_line = chords_line.rstrip() if chords_line else ''
            lyrics.append(lyrics_line)  # get list of inputs
            chords.append(chords_line) 
        lyrics = '\n'.join(lyrics) # list -> str
        chords = '\n'.join(chords)
        update_lyrics_chords(song_id, lyrics, chords)
        return f"<h1> Lyrics and Chords Updated successfully </h1> <br> <a href='/{song_id}/song-transpose'>See song</a> <br> <a href='/'>Home</a>"
        
    else:
        pass

def add_chords_json(song_id, update=False):
    title, lyrics, chords, composers, lyricists = get_song_by_id(song_id)

    if request.method == 'GET':
        if chords == '' or update == False or chords is None:
            chords = '\n'.join(len(lyrics.split('\n')) * [''])
        elif len(chords.split('\n')) != len(lyrics.split('\n')):
            k = len(lyrics.split('\n')) - len(chords.split('\n'))
            chords += k * '\n'

        chords_list = [x + (100 - len(x)) * ' ' for x in chords.split('\n')]
        lyrics_list = lyrics.split('\n')

        return jsonify({
            'title': title,
            'composers': composers,
            'lyricists': lyricists,
            'lyrics_list': lyrics_list,
            'chords_list': chords_list,
            'song_id': song_id,
            'i': 0,
        })

    elif request.method == 'POST':
        lines = len(lyrics.split('\n'))
        lyrics_input = []
        chords_input = []
        for i in range(lines):
            lyrics_line = request.json.get(f'lyricsLine-{i+1}', '')
            chords_line = request.json.get(f'chordsLine-{i+1}', '').rstrip()

            lyrics_input.append(lyrics_line)
            chords_input.append(chords_line)

        lyrics = '\n'.join(lyrics_input)
        chords = '\n'.join(chords_input)

        update_lyrics_chords(song_id, lyrics, chords)

        return jsonify({
            'message': 'Lyrics and Chords updated successfully'
        }), 200

    else:
        return jsonify({
            'error': 'Invalid request method'
        }), 405  # Method Not Allowed     
