"""
Specific Team endpoints for Music Teams - requires enrollment in specific team
"""
from flask import Blueprint, jsonify, g
from ..utils.auth import require_team_access
from ..utils.queries import (
    get_all_composers_specific_team,
    get_all_lyricists_specific_team,
    get_all_songs_specific_team
)

specific_team_bp = Blueprint('specific_team', __name__, url_prefix='/specific_team')


@specific_team_bp.route('/all-composers', methods=['GET'])
@require_team_access
def get_specific_team_composers():
    """
    GET /specific_team/all-composers?team_name=sample_name
    Returns all composers that are in songs in the team specified by team_name.
    Requires authenticated user and enrollment in the specified team.
    """
    try:
        team_name = g.team_name
        composers = get_all_composers_specific_team(team_name)
        return jsonify({
            "composers": composers,
            "count": len(composers),
            "team": team_name,
            "user": g.current_user
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@specific_team_bp.route('/all-lyricists', methods=['GET'])
@require_team_access
def get_specific_team_lyricists():
    """
    GET /specific_team/all-lyricists?team_name=sample_name
    Returns all lyricists that are in songs in the team specified by team_name.
    Requires authenticated user and enrollment in the specified team.
    """
    try:
        team_name = g.team_name
        lyricists = get_all_lyricists_specific_team(team_name)
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists),
            "team": team_name,
            "user": g.current_user
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@specific_team_bp.route('/all-songs', methods=['GET'])
@require_team_access
def get_specific_team_songs():
    """
    GET /specific_team/all-songs?team_name=sample_name
    Returns all songs in the team specified by team_name.
    Requires authenticated user and enrollment in the specified team.
    """
    try:
        team_name = g.team_name
        songs = get_all_songs_specific_team(team_name)
        return jsonify({
            "songs": songs,
            "count": len(songs),
            "team": team_name,
            "user": g.current_user
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500