"""
Main application with new monolith routes
"""
from flask import Flask, g
from monolith.routes.public import public_bp
from monolith.routes.my_teams import my_teams_bp
from monolith.routes.specific_team import specific_team_bp

# Import existing modules to maintain compatibility
from add_lyrics_chords import *
from help_routes import *
from transporto import *
from __init__ import list_url, song_demands_url, recordings_url
from web_scrape import scrape_from_html_to_json

app = Flask(__name__)

# Register new monolith blueprints
app.register_blueprint(public_bp)
app.register_blueprint(my_teams_bp)
app.register_blueprint(specific_team_bp)

# Existing routes (keeping for compatibility)
@app.route('/', methods=['GET'])
def home_route():
    return "<a href='/API'> API </a>  <br><br>"

@app.route('/API', methods=['GET'])
def API_route():
    return render_template('API.html')

@app.route('/API/home', methods=['GET', 'POST'])
def home_route_json():
    return home_json()

# Close database connection at the end of request
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)