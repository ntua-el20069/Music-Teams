from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector

from add_lyrics_chords import *
from help_routes import *
from transporto import *
from __init__ import list_url

#from .accept import *

app = Flask(__name__)
auth = HTTPBasicAuth()
db_name = "songs"

app.jinja_env.filters['zip'] = zip

users = {
    "AN": "ablaoublas"
}

# Verify the username and password for each request
@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]: #or username==get_admin()[0] and password==get_admin()[1]:
        return username


@app.route('/', methods = ['GET'])
def home_route():
    return render_template('API.html')

@app.route('/music-teams', methods = ['GET', 'POST'])
def home_route_json():
    return home_json()



@app.route('/music-teams/add-song', methods = ['GET', 'POST'])

def add_song_route_json():
    return add_lyrics_json()




@app.route('/<song_id>/update-lyrics', methods = ['GET', 'POST'])

def update_lyrics_route(song_id):
    return add_lyrics(song_id=song_id, update=True)



@app.route('/music-teams/<song_id>/add-chords', methods = ['GET', 'POST'])

def add_chords_route_json(song_id):
    return add_chords_json(song_id)



@app.route('/<song_id>/update-chords', methods = ['GET', 'POST'])

def update_chords_route(song_id):
    return add_chords(song_id, update = True)




@app.route('/<song_id>/song-transpose', methods = ['GET', 'POST'])
def song_transpose_route(song_id):
    return song_transpose(song_id)

@app.route('/<song_id>/permanent-transporto', methods = ['GET', 'POST'])

def permanent_transporto_route(song_id):
    return song_transpose(song_id, permanent=True)


@app.route('/live')
def live_route():
    songs = songs_list()
    songs_with_index = zip(range(len(songs)), songs)
    return render_template('live.html', songs_with_index=songs_with_index)

@app.route('/live/<int:num>')
def live_song(num: int):
    songs = songs_list()
    #print(songs)
    index_error_message = 'Invalid index, return back! <br>'
    if num < 0 : return index_error_message
    try:
        song_title = songs[num]
    except:
        return index_error_message
    try:
        id = get_id_by_title(song_title)
        return song_transpose(id, live = 1, live_id = num)
    except:
        return f'{song_title} does not exist in the Database, try to find lyrics somewhere else! <br>'
    
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)
