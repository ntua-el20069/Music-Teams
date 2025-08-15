"""
Enhanced test application that connects to the actual database for public endpoints.
"""

from flask import Flask, jsonify, request
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from __init__ import get_db
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False
    print("Warning: Database connection not available. Using mock data.")

app = Flask(__name__)

# Mock data for testing when DB is not available
MOCK_COMPOSERS = ["Μίκης Θεοδωράκης", "Guns and Roses", "Lennon", "MacCartney"]
MOCK_LYRICISTS = ["Ρίτσος", "Μίκης Θεοδωράκης", "Lennon", "MacCartney"]
MOCK_SONGS = ["Μαργαρίτα Μαργαρώ", "A day in life", "Sweet child o' mine"]

def get_current_user_mock():
    """Mock authentication - always returns test user."""
    return "AntonisNikos"

def get_teams_of_user_mock(username):
    """Mock team function - returns empty list."""
    return []

def team_if_enrolled_mock(username, team_name):
    """Mock team enrollment check - always returns False."""
    return False

def all_public_composers_db():
    """Get all composers from public songs using database."""
    if not DB_AVAILABLE:
        return MOCK_COMPOSERS
        
    try:
        db = get_db()
        cursor = db.cursor()
        sql = """
            SELECT DISTINCT c.name 
            FROM composer c 
            JOIN wrotemusic wm ON c.name = wm.composer 
            JOIN song s ON wm.song_id = s.id 
            WHERE s.public = 1
            ORDER BY c.name
        """
        cursor.execute(sql)
        composers = [x[0] for x in cursor.fetchall()]
        cursor.close()
        return composers
    except Exception as e:
        print(f"Database error: {e}")
        return MOCK_COMPOSERS

def all_public_lyricists_db():
    """Get all lyricists from public songs using database."""
    if not DB_AVAILABLE:
        return MOCK_LYRICISTS
        
    try:
        db = get_db()
        cursor = db.cursor()
        sql = """
            SELECT DISTINCT l.name 
            FROM lyricist l 
            JOIN wrotelyrics wl ON l.name = wl.lyricist 
            JOIN song s ON wl.song_id = s.id 
            WHERE s.public = 1
            ORDER BY l.name
        """
        cursor.execute(sql)
        lyricists = [x[0] for x in cursor.fetchall()]
        cursor.close()
        return lyricists
    except Exception as e:
        print(f"Database error: {e}")
        return MOCK_LYRICISTS

def all_public_songs_db():
    """Get all public songs using database."""
    if not DB_AVAILABLE:
        return MOCK_SONGS
        
    try:
        db = get_db()
        cursor = db.cursor()
        sql = "SELECT title FROM song WHERE public = 1 ORDER BY title"
        cursor.execute(sql)
        songs = [x[0] for x in cursor.fetchall()]
        cursor.close()
        return songs
    except Exception as e:
        print(f"Database error: {e}")
        return MOCK_SONGS

# Public endpoints
@app.route('/public/all-composers', methods=['GET'])
def get_all_public_composers():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    composers = all_public_composers_db()
    return jsonify({
        "composers": composers,
        "count": len(composers),
        "source": "database" if DB_AVAILABLE else "mock"
    }), 200

@app.route('/public/all-lyricists', methods=['GET'])
def get_all_public_lyricists():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    lyricists = all_public_lyricists_db()
    return jsonify({
        "lyricists": lyricists,
        "count": len(lyricists),
        "source": "database" if DB_AVAILABLE else "mock"
    }), 200

@app.route('/public/all-songs', methods=['GET'])
def get_all_public_songs():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    songs = all_public_songs_db()
    return jsonify({
        "songs": songs,
        "count": len(songs),
        "source": "database" if DB_AVAILABLE else "mock"
    }), 200

# My teams endpoints
@app.route('/myteams/all-composers', methods=['GET'])
def get_all_myteams_composers():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "composers": [],  # Empty since no teams implemented yet
        "count": 0,
        "user_teams": user_teams,
        "note": "Team functionality not yet implemented"
    }), 200

@app.route('/myteams/all-lyricists', methods=['GET'])
def get_all_myteams_lyricists():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "lyricists": [],  # Empty since no teams implemented yet
        "count": 0,
        "user_teams": user_teams,
        "note": "Team functionality not yet implemented"
    }), 200

@app.route('/myteams/all-songs', methods=['GET'])
def get_all_myteams_songs():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "songs": [],  # Empty since no teams implemented yet
        "count": 0,
        "user_teams": user_teams,
        "note": "Team functionality not yet implemented"
    }), 200

# Specific team endpoints
@app.route('/specific_team/all-composers', methods=['GET'])
def get_all_team_composers():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    team_name = request.args.get('team_name')
    if not team_name:
        return jsonify({"error": "team_name parameter is required"}), 400
    
    if not team_if_enrolled_mock(current_user, team_name):
        return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
    
    return jsonify({
        "composers": [],
        "count": 0,
        "team_name": team_name,
        "note": "Team functionality not yet implemented"
    }), 200

@app.route('/specific_team/all-lyricists', methods=['GET'])
def get_all_team_lyricists():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    team_name = request.args.get('team_name')
    if not team_name:
        return jsonify({"error": "team_name parameter is required"}), 400
    
    if not team_if_enrolled_mock(current_user, team_name):
        return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
    
    return jsonify({
        "lyricists": [],
        "count": 0,
        "team_name": team_name,
        "note": "Team functionality not yet implemented"
    }), 200

@app.route('/specific_team/all-songs', methods=['GET'])
def get_all_team_songs():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    team_name = request.args.get('team_name')
    if not team_name:
        return jsonify({"error": "team_name parameter is required"}), 400
    
    if not team_if_enrolled_mock(current_user, team_name):
        return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
    
    return jsonify({
        "songs": [],
        "count": 0,
        "team_name": team_name,
        "note": "Team functionality not yet implemented"
    }), 200

# Home endpoint
@app.route('/')
def home():
    return {
        "message": "Music Teams All-Endpoints API",
        "database_status": "connected" if DB_AVAILABLE else "not available",
        "endpoints": {
            "public": [
                "GET /public/all-composers",
                "GET /public/all-lyricists", 
                "GET /public/all-songs"
            ],
            "myteams": [
                "GET /myteams/all-composers",
                "GET /myteams/all-lyricists",
                "GET /myteams/all-songs"
            ],
            "specific_team": [
                "GET /specific_team/all-composers?team_name=<name>",
                "GET /specific_team/all-lyricists?team_name=<name>",
                "GET /specific_team/all-songs?team_name=<name>"
            ]
        }
    }

if __name__ == "__main__":
    app.run(debug=True, port=5001)