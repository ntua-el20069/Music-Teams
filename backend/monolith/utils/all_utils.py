"""
Utility functions for getting all composers, lyricists, and songs
for different scenarios: public, specific team, and user's teams.
"""

import sys
import os
# Add the backend directory to the Python path to import __init__
backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, backend_dir)

try:
    from __init__ import get_db
except ImportError:
    # If import fails, provide a mock function for testing
    def get_db():
        raise NotImplementedError("Database connection not available")

from .team_utils import get_teams_of_user


def all_public_composers() -> list:
    """
    Get all composers that are in public songs.
    
    Returns:
        List of composer names from public songs
    """
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


def all_public_lyricists() -> list:
    """
    Get all lyricists that are in public songs.
    
    Returns:
        List of lyricist names from public songs
    """
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


def all_public_songs() -> list:
    """
    Get all public songs.
    
    Returns:
        List of song titles that are public
    """
    db = get_db()
    cursor = db.cursor()
    sql = "SELECT title FROM song WHERE public = 1 ORDER BY title"
    cursor.execute(sql)
    songs = [x[0] for x in cursor.fetchall()]
    cursor.close()
    return songs


def all_team_composers(team_name: str) -> list:
    """
    Get all composers that are in songs in the specified team.
    
    Args:
        team_name: Name of the team
        
    Returns:
        List of composer names from songs in the team
        
    Note: This is a placeholder implementation until team-song relationships are created.
    Currently returns empty list.
    """
    # TODO: Implement actual team-song relationship queries
    # db = get_db()
    # cursor = db.cursor()
    # sql = """
    #     SELECT DISTINCT c.name 
    #     FROM composer c 
    #     JOIN wrotemusic wm ON c.name = wm.composer 
    #     JOIN song s ON wm.song_id = s.id 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name = %s
    #     ORDER BY c.name
    # """
    # cursor.execute(sql, (team_name,))
    # composers = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return composers
    
    # Placeholder return
    return []


def all_team_lyricists(team_name: str) -> list:
    """
    Get all lyricists that are in songs in the specified team.
    
    Args:
        team_name: Name of the team
        
    Returns:
        List of lyricist names from songs in the team
        
    Note: This is a placeholder implementation until team-song relationships are created.
    Currently returns empty list.
    """
    # TODO: Implement actual team-song relationship queries
    # db = get_db()
    # cursor = db.cursor()
    # sql = """
    #     SELECT DISTINCT l.name 
    #     FROM lyricist l 
    #     JOIN wrotelyrics wl ON l.name = wl.lyricist 
    #     JOIN song s ON wl.song_id = s.id 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name = %s
    #     ORDER BY l.name
    # """
    # cursor.execute(sql, (team_name,))
    # lyricists = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return lyricists
    
    # Placeholder return
    return []


def all_team_songs(team_name: str) -> list:
    """
    Get all songs in the specified team.
    
    Args:
        team_name: Name of the team
        
    Returns:
        List of song titles in the team
        
    Note: This is a placeholder implementation until team-song relationships are created.
    Currently returns empty list.
    """
    # TODO: Implement actual team-song relationship queries
    # db = get_db()
    # cursor = db.cursor()
    # sql = """
    #     SELECT s.title 
    #     FROM song s 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name = %s
    #     ORDER BY s.title
    # """
    # cursor.execute(sql, (team_name,))
    # songs = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return songs
    
    # Placeholder return
    return []


def all_myteams_composers(username: str) -> list:
    """
    Get all composers that are in songs in teams in which the user participates.
    
    Args:
        username: Username of the user
        
    Returns:
        List of composer names from songs in user's teams
        
    Note: This is a placeholder implementation until team functionality is complete.
    Currently returns empty list.
    """
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    # TODO: Implement actual queries once team tables exist
    # db = get_db()
    # cursor = db.cursor()
    # placeholders = ','.join(['%s'] * len(user_teams))
    # sql = f"""
    #     SELECT DISTINCT c.name 
    #     FROM composer c 
    #     JOIN wrotemusic wm ON c.name = wm.composer 
    #     JOIN song s ON wm.song_id = s.id 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name IN ({placeholders})
    #     ORDER BY c.name
    # """
    # cursor.execute(sql, user_teams)
    # composers = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return composers
    
    # Placeholder return
    return []


def all_myteams_lyricists(username: str) -> list:
    """
    Get all lyricists that are in songs in teams in which the user participates.
    
    Args:
        username: Username of the user
        
    Returns:
        List of lyricist names from songs in user's teams
        
    Note: This is a placeholder implementation until team functionality is complete.
    Currently returns empty list.
    """
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    # TODO: Implement actual queries once team tables exist
    # db = get_db()
    # cursor = db.cursor()
    # placeholders = ','.join(['%s'] * len(user_teams))
    # sql = f"""
    #     SELECT DISTINCT l.name 
    #     FROM lyricist l 
    #     JOIN wrotelyrics wl ON l.name = wl.lyricist 
    #     JOIN song s ON wl.song_id = s.id 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name IN ({placeholders})
    #     ORDER BY l.name
    # """
    # cursor.execute(sql, user_teams)
    # lyricists = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return lyricists
    
    # Placeholder return
    return []


def all_myteams_songs(username: str) -> list:
    """
    Get all songs in teams in which the user participates.
    
    Args:
        username: Username of the user
        
    Returns:
        List of song titles from user's teams
        
    Note: This is a placeholder implementation until team functionality is complete.
    Currently returns empty list.
    """
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    # TODO: Implement actual queries once team tables exist
    # db = get_db()
    # cursor = db.cursor()
    # placeholders = ','.join(['%s'] * len(user_teams))
    # sql = f"""
    #     SELECT s.title 
    #     FROM song s 
    #     JOIN team_songs ts ON s.id = ts.song_id
    #     WHERE ts.team_name IN ({placeholders})
    #     ORDER BY s.title
    # """
    # cursor.execute(sql, user_teams)
    # songs = [x[0] for x in cursor.fetchall()]
    # cursor.close()
    # return songs
    
    # Placeholder return
    return []