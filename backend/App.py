from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector
#import psycopg2 

from add_lyrics_chords import *
from help_routes import *
from transporto import *
from __init__ import list_url

#from .accept import *

app = Flask(__name__)
auth = HTTPBasicAuth()
db_name = "songs"

app.jinja_env.filters['zip'] = zip


''' # for MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",                       # that's because I do not use a password... you may change it for your DBMS
    database=db_name,   # a database I created to play with...
    charset = "utf8",
    use_unicode = True
)

cursor = db.cursor()
cursor.execute("SET NAMES utf8;")
cursor.execute("SET CHARACTER SET utf8;")
cursor.execute("SET character_set_connection = utf8;")
cursor.close()
'''

'''  # for PostgreSQL

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
db = psycopg2.connect(
    host="localhost",
    database=db_name,   # a database I created to play with...
    user="root",
    password=""     # that's because I do not use a password... you may change it for your DBMS
)
'''

users = {
    "AN": "ablaoublas"
}

# Verify the username and password for each request
@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]: #or username==get_admin()[0] and password==get_admin()[1]:
        return username


@app.route('/', methods = ['GET', 'POST'])
def home_route():
    return home()

@app.route('/music-teams', methods = ['GET', 'POST'])
def home_route_json():
    return home_json()

@app.route('/add-song', methods = ['GET', 'POST'])
@auth.login_required
def add_song_route():
    return add_lyrics()

@app.route('/music-teams/add-song', methods = ['GET', 'POST'])
@auth.login_required
def add_song_json_route():
    return add_lyrics_json()

@app.route('/<song_id>/update-lyrics', methods = ['GET', 'POST'])
@auth.login_required
def update_lyrics_route(song_id):
    return add_lyrics(song_id=song_id, update=True)

@app.route('/<song_id>/add-chords', methods = ['GET', 'POST'])
@auth.login_required
def add_chords_route(song_id):
    return add_chords(song_id)

@app.route('/<song_id>/update-chords', methods = ['GET', 'POST'])
@auth.login_required
def update_chords_route(song_id):
    return add_chords(song_id, update = True)


@app.route('/<song_id>/song-transpose', methods = ['GET', 'POST'])
def song_transpose_route(song_id):
    return song_transpose(song_id)

@app.route('/<song_id>/permanent-transporto', methods = ['GET', 'POST'])
@auth.login_required
def permanent_transporto_route(song_id):
    return song_transpose(song_id, permanent=True)

@app.route('/previous/<int:song_id>')
def previous(song_id):
    if song_id == 0: return 'No other previous song'
    previous_song_id = song_id - 1
    return redirect(f'/{previous_song_id}/song-transpose')

@app.route('/next/<int:song_id>')
def next(song_id):
    next_song_id = song_id + 1
    return redirect(f'/{next_song_id}/song-transpose')

@app.route('/previous-live/<int:live_id>')
def previous_live(live_id):
    if live_id == 0: return 'No other previous song'
    previous_live_id = live_id - 1
    return redirect(f'/live/{previous_live_id}')

@app.route('/next-live/<int:live_id>')
def next_live(live_id):
    next_live_id = live_id + 1
    return redirect(f'/live/{next_live_id}')

@app.route('/list', methods=['GET', 'POST'])
@auth.login_required
def list():
    if request.method == 'GET':
        return render_template('list.html', songs=songs_list(), all_songs = all_songs())
    # POST
    out = request.form.get('songList')
    with open(list_url(), 'w') as file:
        file.write(out)
    return 'Saved Succesfully  <br> <a href="/list">List</a>   <br><br>' + out.replace('\n', '<br>')

@app.route('/check')
def check():
    with open(list_url(), 'r', encoding='utf-8') as file:
        songs = file.read()
    songs = songs.split('\n') 
    if songs[-1] == '': songs = songs[:-1]
    if songs[0] == '': songs = songs[1:]
    
    db_songs = all_songs()
    out = "The following songs from the list are not in the Database: <br>"
    for song in songs:
        if song not in db_songs: 
            out += f"{song} <br>"
    return out

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
