from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth
import mysql.connector

from add_lyrics_chords import *
from help_routes import *
from transporto import *
from __init__ import list_url
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





################################################################


if __name__ == '__main__':
    app.run(debug=True, port=5001)
