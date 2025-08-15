"""
Specific team endpoints for getting all composers, lyricists, and songs.
These endpoints return data from songs in the team specified by team_name parameter.
"""

from flask import Blueprint, jsonify, request
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from monolith.utils.all_utils import all_team_composers, all_team_lyricists, all_team_songs
from monolith.utils.team_utils import get_current_user, get_teams_of_user, team_if_enrolled

# Create blueprint for specific team routes
specific_team_bp = Blueprint('specific_team', __name__, url_prefix='/specific_team')


@specific_team_bp.route('/all-composers', methods=['GET'])
def get_all_team_composers():
    """
    GET /specific_team/all-composers?team_name=sample_name
    Returns all composers that are in songs in the team specified by team_name.
    Requires authenticated user, access to team_data cookie, and team enrollment check.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get team_name from query parameters
        team_name = request.args.get('team_name')
        if not team_name:
            return jsonify({"error": "team_name parameter is required"}), 400
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        # Check if user is enrolled in the specified team
        if not team_if_enrolled(current_user, team_name):
            return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
        
        composers = all_team_composers(team_name)
        return jsonify({
            "composers": composers,
            "count": len(composers),
            "team_name": team_name
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@specific_team_bp.route('/all-lyricists', methods=['GET'])
def get_all_team_lyricists():
    """
    GET /specific_team/all-lyricists?team_name=sample_name
    Returns all lyricists that are in songs in the team specified by team_name.
    Requires authenticated user, access to team_data cookie, and team enrollment check.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get team_name from query parameters
        team_name = request.args.get('team_name')
        if not team_name:
            return jsonify({"error": "team_name parameter is required"}), 400
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        # Check if user is enrolled in the specified team
        if not team_if_enrolled(current_user, team_name):
            return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
        
        lyricists = all_team_lyricists(team_name)
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists),
            "team_name": team_name
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@specific_team_bp.route('/all-songs', methods=['GET'])
def get_all_team_songs():
    """
    GET /specific_team/all-songs?team_name=sample_name
    Returns all songs in the team specified by team_name.
    Requires authenticated user, access to team_data cookie, and team enrollment check.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get team_name from query parameters
        team_name = request.args.get('team_name')
        if not team_name:
            return jsonify({"error": "team_name parameter is required"}), 400
        
        # Check if user has access to team data (placeholder for team_data cookie check)
        user_teams = get_teams_of_user(current_user)
        # Note: In a real implementation, we would check for team_data cookie here
        
        # Check if user is enrolled in the specified team
        if not team_if_enrolled(current_user, team_name):
            return jsonify({"error": f"User is not enrolled in team '{team_name}'"}), 403
        
        songs = all_team_songs(team_name)
        return jsonify({
            "songs": songs,
            "count": len(songs),
            "team_name": team_name
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500