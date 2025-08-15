"""
My Teams endpoints for Music Teams - requires team membership
"""
from flask import Blueprint, jsonify, g
from ..utils.auth import require_auth
from ..utils.queries import (
    get_all_composers_user_teams,
    get_all_lyricists_user_teams,
    get_all_songs_user_teams
)

my_teams_bp = Blueprint('my_teams', __name__, url_prefix='/my_teams')


@my_teams_bp.route('/all-composers', methods=['GET'])
@require_auth
def get_my_teams_composers():
    """
    GET /my_teams/all-composers
    Returns all composers that are in songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        username = g.current_user
        composers = get_all_composers_user_teams(username)
        return jsonify({
            "composers": composers,
            "count": len(composers),
            "user": username
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@my_teams_bp.route('/all-lyricists', methods=['GET'])
@require_auth
def get_my_teams_lyricists():
    """
    GET /my_teams/all-lyricists
    Returns all lyricists that are in songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        username = g.current_user
        lyricists = get_all_lyricists_user_teams(username)
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists),
            "user": username
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@my_teams_bp.route('/all-songs', methods=['GET'])
@require_auth
def get_my_teams_songs():
    """
    GET /my_teams/all-songs
    Returns all songs in teams in which the user participates.
    Requires authenticated user and access to team_data cookie.
    """
    try:
        username = g.current_user
        songs = get_all_songs_user_teams(username)
        return jsonify({
            "songs": songs,
            "count": len(songs),
            "user": username
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500