from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector

mode = 'local'     # CHANGE             #  mode = 'local' for local PC database, mode = 'web' for PythonAnywhere Database

def get_db():
    db_name = "songs" if mode=='local' else "nikolaospapa3$musicteams"
    if 'db' not in g:
        # for MySQL
        if mode == 'local':
            g.db = mysql.connector.connect(
                port = 3307,
                host="localhost",
                user="root",
                password="",  # change it for your DBMS
                database=db_name, 
                charset="utf8",
                use_unicode=True
            )
        else:
            g.db = mysql.connector.connect(
                host="nikolaospapa3.mysql.pythonanywhere-services.com",
                user="nikolaospapa3",
                password="",  # CHANGE  # change it for your DBMS
                database=db_name,   
                charset = "utf8",
                use_unicode = True
            )
        g.db.cursor().execute("SET NAMES utf8;")
        g.db.cursor().execute("SET CHARACTER SET utf8;")
        g.db.cursor().execute("SET character_set_connection = utf8;")
    return g.db

def list_url():
    return 'list.txt' if mode=='local' else '/home/nikolaospapa3/ChordPose/list.txt'

def song_demands_url():
    return 'backend/lists/song-demands.txt' if mode=='local' else '/home/nikolaospapa3/Music-Teams/backend/lists/song-demands.txt'

def recordings_url():
    return '/home/nikolaospapa3/Documents/web-dev/Mobile/Music-Teams/backend/recordings' if mode=='local' else '/home/nikolaospapa3/recordings'