"""
Public endpoints for Music Teams - no team membership required
"""
from flask import Blueprint, jsonify, g
from ..utils.auth import require_auth
from ..utils.queries import (
    get_all_composers_public,
    get_all_lyricists_public,
    get_all_songs_public
)

public_bp = Blueprint('public', __name__, url_prefix='/public')


@public_bp.route('/all-composers', methods=['GET'])
@require_auth
def get_public_composers():
    """
    GET /public/all-composers
    Returns all composers that are in public songs.
    Requires authenticated user.
    """
    try:
        composers = get_all_composers_public()
        return jsonify({
            "composers": composers,
            "count": len(composers)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@public_bp.route('/all-lyricists', methods=['GET'])
@require_auth
def get_public_lyricists():
    """
    GET /public/all-lyricists
    Returns all lyricists that are in public songs.
    Requires authenticated user.
    """
    try:
        lyricists = get_all_lyricists_public()
        return jsonify({
            "lyricists": lyricists,
            "count": len(lyricists)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@public_bp.route('/all-songs', methods=['GET'])
@require_auth
def get_public_songs():
    """
    GET /public/all-songs
    Returns all public songs.
    Requires authenticated user.
    """
    try:
        songs = get_all_songs_public()
        return jsonify({
            "songs": songs,
            "count": len(songs)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500