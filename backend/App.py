from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector

from add_lyrics_chords import *
from help_routes import *
from transporto import *
from __init__ import list_url, song_demands_url
from web_scrape import scrape_from_html_to_json

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
    return "<a href='/API'> API </a>  <br><br>"

@app.route('/API', methods = ['GET'])
def API_route():
    return render_template('API.html')

@app.route('/API/home', methods = ['GET', 'POST'])
def home_route_json():
    return home_json()

@app.route('/API/add-song', methods = ['GET', 'POST'])

def add_song_route_json():
    return add_lyrics_json()

@app.route('/API/<song_id>/add-chords', methods = ['GET', 'POST'])

def add_chords_route_json(song_id):
    return add_chords_json(song_id)

@app.route('/API/<song_id>/song-transpose', methods = ['GET', 'POST'])
def song_transpose_route_json(song_id):
    return song_transpose_json(song_id)

@app.route('/API/webscrape', methods = ['POST'])
def webscrape_route():
    html = request.data.decode('utf-8')
    return scrape_from_html_to_json(html)

# Set the upload folder
#base_url = '/home/nikolaospapa3/Documents/web-dev/Mobile/Music-Teams/backend/'
base_url = '/home/nikolaospapa3/Music-Teams/backend/'
app.config['UPLOAD_FOLDER'] = base_url + 'recordings'

@app.route('/<song_id>/add-recording')
def recording(song_id):
    return render_template('recording.html', song_id = song_id)

@app.route('/API/<song_id>/upload', methods=['POST'])
def upload_file_json(song_id):
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            file_path = f"{app.config['UPLOAD_FOLDER']}/{song_id}-{uploaded_file.filename}"
            uploaded_file.save(file_path)
            return jsonify({"message": "File uploaded successfully!", "file_path": file_path})

    return jsonify({"error": "No file uploaded or something went wrong."})

@app.route('/API/make-song-demand', methods=['POST'])
def make_song_demand():
    request_data = request.get_json()
    if request_data is None or 'title' not in request_data:
        return jsonify({"error": "Invalid JSON format or missing 'title' key"}), 400  # Bad Request
    demanded = request_data.get('title')
    with open(song_demands_url(), 'a') as file: file.write('') # just to make the file if it does not exist
    with open(song_demands_url(), 'r') as file:
        #if demanded in file.read(): return jsonify({"error": "This song has been already demanded"}), 400  # Bad Request
        songs = file.read().split('\n')
        if len(songs) > 11: 
            last_songs = songs[-2:-12:-1]
            if demanded in last_songs: return jsonify({"error": "This song has been already demanded"}), 400  # Bad Request
    with open(song_demands_url(), 'a') as file:
        file.write(demanded + '\n')
    return jsonify({"message": f"Demanded song {demanded}"}), 200  

@app.route('/API/recent-song-demands', methods=['GET'])
def recent_song_demands():
    with open(song_demands_url(), 'r') as file:
        demanded = file.read().split('\n')
    print(demanded)
    if len(demanded) > 11:
        demanded = demanded[-11::1] # take only the 10 last song demands 
    demanded_songs = '\n'.join(demanded[-2::-1]) if len(demanded) >= 2  else '' # the inverse list with [0][1] ... [len] from the most recent to the older

    print(demanded_songs)
    return jsonify({"demanded-songs": f"{demanded_songs}"}), 200 

################################################################


if __name__ == '__main__':
    app.run(debug=True, port=5001)
