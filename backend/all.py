from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort
from flask_httpauth import HTTPBasicAuth
import mysql.connector
#import psycopg2 
from __init__ import get_db, list_url

def all_composers() -> list:
    db = get_db()
    cursor = db.cursor()
    sql = f"select name from composer"
    cursor.execute(sql)
    composers = [x[0] for x in cursor.fetchall()]
    return composers

def all_lyricists() -> list:
    db = get_db()
    cursor = db.cursor()
    sql = f"select name from lyricist"
    cursor.execute(sql)
    lyricists = [x[0] for x in cursor.fetchall()]
    return lyricists 

def all_songs() -> list:
    db = get_db()
    cursor = db.cursor()
    sql = f"select title from song"
    cursor.execute(sql)
    songs = [x[0] for x in cursor.fetchall()]
    return songs 

def songs_list() -> list:
    with open(list_url(),'r') as file:
        content = file.read()
        songs = content.split('\n')
        if songs[-1] == '': return songs[:-1]
        if songs[0] == '': return songs[1:]
        return songs
