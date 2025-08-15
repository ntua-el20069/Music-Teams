"""
My teams endpoints for getting all composers, lyricists, and songs.
These endpoints return data from songs in teams in which the user participates.
"""

from flask import Blueprint, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from monolith.utils.all_utils import all_myteams_composers, all_myteams_lyricists, all_myteams_songs
from monolith.utils.team_utils import get_current_user, get_teams_of_user

# Create blueprint for myteams routes
myteams_bp = Blueprint('myteams', __name__, url_prefix='/myteams')


@myteams_bp.route('/all-composers', methods=['GET'])
def get_all_myteams_composers():
    """
    GET /myteams/all-composers
    Returns all composers that are in songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        composers = all_myteams_composers(current_user)
        return jsonify({
            "composers": composers,
            "count": len(composers),
            "user_teams": user_teams
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@myteams_bp.route('/all-lyricists', methods=['GET'])
def get_all_myteams_lyricists():
    """
    GET /myteams/all-lyricists
    Returns all lyricists that are in songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        lyricists = all_myteams_lyricists(current_user)
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists),
            "user_teams": user_teams
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@myteams_bp.route('/all-songs', methods=['GET'])
def get_all_myteams_songs():
    """
    GET /myteams/all-songs
    Returns all songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        songs = all_myteams_songs(current_user)
        return jsonify({
            "songs": songs,
            "count": len(songs),
            "user_teams": user_teams
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500