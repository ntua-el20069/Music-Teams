"""
Authentication and team management utilities for Music Teams
"""
from flask import request, jsonify, g
from functools import wraps
import base64
from __init__ import get_db


def get_current_user():
    """
    Extract current user from HTTP Basic Auth.
    Returns username or None if not authenticated.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return None
    
    try:
        # Decode Basic Auth
        encoded_credentials = auth_header.split(' ')[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = decoded_credentials.split(':', 1)
        
        # Verify credentials against database
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT username FROM user WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        
        if result:
            return username
        return None
    except Exception:
        return None


def get_teams_of_user(username):
    """
    Get list of teams that a user belongs to.
    For now, implements a simple mapping based on username.
    In a full implementation, this would query a user_teams table.
    """
    if not username:
        return []
    
    # Simple team mapping - in production this would be database-driven
    # For now, create some example teams based on user
    team_mapping = {
        'AntonisNikos': ['team1', 'team2', 'default_team'],
        # Add more users as needed
    }
    
    return team_mapping.get(username, ['default_team'])


def team_if_enrolled(username, team_name):
    """
    Check if user is enrolled in a specific team.
    Returns team_name if enrolled, None otherwise.
    """
    if not username or not team_name:
        return None
    
    user_teams = get_teams_of_user(username)
    if team_name in user_teams:
        return team_name
    return None


def get_songs_in_teams(team_names):
    """
    Get all song IDs that belong to specified teams.
    For now, maps songs to teams based on made_by field.
    In production, this would use a proper song_teams table.
    """
    if not team_names:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    # For now, consider songs as belonging to teams based on their creator
    # This is a simplified implementation
    song_ids = []
    
    # Get songs made by users in these teams
    team_users = []
    for team in team_names:
        if team == 'team1':
            team_users.extend(['AntonisNikos'])
        elif team == 'team2':
            team_users.extend(['AntonisNikos'])
        elif team == 'default_team':
            team_users.extend(['AntonisNikos'])
    
    if team_users:
        placeholders = ','.join(['%s'] * len(team_users))
        cursor.execute(f"SELECT id FROM song WHERE made_by IN ({placeholders})", team_users)
        song_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.close()
    return song_ids


def get_songs_in_specific_team(team_name):
    """
    Get all song IDs that belong to a specific team.
    """
    if not team_name:
        return []
    
    return get_songs_in_teams([team_name])


def require_auth(f):
    """
    Decorator to require authentication for routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = get_current_user()
        if not username:
            return jsonify({"error": "Authentication required"}), 401
        g.current_user = username
        return f(*args, **kwargs)
    return decorated_function


def require_team_access(f):
    """
    Decorator to require team access for routes with team_name parameter.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = get_current_user()
        if not username:
            return jsonify({"error": "Authentication required"}), 401
        
        team_name = request.args.get('team_name')
        if not team_name:
            return jsonify({"error": "team_name parameter required"}), 400
        
        if not team_if_enrolled(username, team_name):
            return jsonify({"error": f"User not enrolled in team {team_name}"}), 403
        
        g.current_user = username
        g.team_name = team_name
        return f(*args, **kwargs)
    return decorated_function