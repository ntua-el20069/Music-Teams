"""
Public endpoints for getting all composers, lyricists, and songs.
These endpoints return data from public songs only.
"""

from flask import Blueprint, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from monolith.utils.all_utils import all_public_composers, all_public_lyricists, all_public_songs
from monolith.utils.team_utils import get_current_user

# Create blueprint for public routes
public_bp = Blueprint('public', __name__, url_prefix='/public')


@public_bp.route('/all-composers', methods=['GET'])
def get_all_public_composers():
    """
    GET /public/all-composers
    Returns all composers that are in public songs.
    Requires authenticated user.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        composers = all_public_composers()
        return jsonify({
            "composers": composers,
            "count": len(composers)
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@public_bp.route('/all-lyricists', methods=['GET'])
def get_all_public_lyricists():
    """
    GET /public/all-lyricists
    Returns all lyricists that are in public songs.
    Requires authenticated user.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        lyricists = all_public_lyricists()
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists)
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@public_bp.route('/all-songs', methods=['GET'])
def get_all_public_songs():
    """
    GET /public/all-songs
    Returns all public songs.
    Requires authenticated user.
    """
    try:
        # Check if user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        songs = all_public_songs()
        return jsonify({
            "songs": songs,
            "count": len(songs)
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500