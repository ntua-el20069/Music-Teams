"""
Simplified test application that doesn't require database connection.
This is for testing the endpoint structure and routing.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for testing
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

# Public endpoints
@app.route('/public/all-composers', methods=['GET'])
def get_all_public_composers():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    return jsonify({
        "composers": MOCK_COMPOSERS,
        "count": len(MOCK_COMPOSERS)
    }), 200

@app.route('/public/all-lyricists', methods=['GET'])
def get_all_public_lyricists():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    return jsonify({
        "lyricists": MOCK_LYRICISTS,
        "count": len(MOCK_LYRICISTS)
    }), 200

@app.route('/public/all-songs', methods=['GET'])
def get_all_public_songs():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    return jsonify({
        "songs": MOCK_SONGS,
        "count": len(MOCK_SONGS)
    }), 200

# My teams endpoints
@app.route('/myteams/all-composers', methods=['GET'])
def get_all_myteams_composers():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "composers": [],  # Empty since no teams
        "count": 0,
        "user_teams": user_teams
    }), 200

@app.route('/myteams/all-lyricists', methods=['GET'])
def get_all_myteams_lyricists():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "lyricists": [],  # Empty since no teams
        "count": 0,
        "user_teams": user_teams
    }), 200

@app.route('/myteams/all-songs', methods=['GET'])
def get_all_myteams_songs():
    current_user = get_current_user_mock()
    if not current_user:
        return jsonify({"error": "Authentication required"}), 401
    
    user_teams = get_teams_of_user_mock(current_user)
    
    return jsonify({
        "songs": [],  # Empty since no teams
        "count": 0,
        "user_teams": user_teams
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
        "team_name": team_name
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
        "team_name": team_name
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
        "team_name": team_name
    }), 200

# Home endpoint
@app.route('/')
def home():
    return {
        "message": "Music Teams All-Endpoints API",
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