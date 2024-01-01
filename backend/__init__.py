from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector



def get_db():
    db_name = "songs"
    if 'db' not in g:
        # for MySQL
        g.db = mysql.connector.connect(
            port = 3307,
            host="localhost",
            user="root",
            password="",  # that's because I do not use a password... you may change it for your DBMS
            database=db_name,  # a database I created to play with...
            charset="utf8",
            use_unicode=True
        )
        g.db.cursor().execute("SET NAMES utf8;")
        g.db.cursor().execute("SET CHARACTER SET utf8;")
        g.db.cursor().execute("SET character_set_connection = utf8;")
    return g.db

def list_url():
    #return '/home/nikolaospapa3/ChordPose/list.txt'
    return 'list.txt'