"""
Database query utilities for getting all composers, lyricists, and songs
"""
from __init__ import get_db
from .auth import get_teams_of_user, get_songs_in_teams, get_songs_in_specific_team


def get_all_composers_public():
    """
    Returns all composers that are in public songs.
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
    composers = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return composers


def get_all_lyricists_public():
    """
    Returns all lyricists that are in public songs.
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
    lyricists = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return lyricists


def get_all_songs_public():
    """
    Returns all public songs with basic information.
    """
    db = get_db()
    cursor = db.cursor()
    
    sql = """
    SELECT id, title, made_by
    FROM song
    WHERE public = 1
    ORDER BY title
    """
    
    cursor.execute(sql)
    songs = []
    for row in cursor.fetchall():
        songs.append({
            'id': row[0],
            'title': row[1],
            'made_by': row[2]
        })
    cursor.close()
    
    return songs


def get_all_composers_user_teams(username):
    """
    Returns all composers that are in songs in teams in which the user participates.
    """
    if not username:
        return []
    
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    team_song_ids = get_songs_in_teams(user_teams)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT DISTINCT c.name 
    FROM composer c
    JOIN wrotemusic wm ON c.name = wm.composer
    WHERE wm.song_id IN ({placeholders})
    ORDER BY c.name
    """
    
    cursor.execute(sql, team_song_ids)
    composers = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return composers


def get_all_lyricists_user_teams(username):
    """
    Returns all lyricists that are in songs in teams in which the user participates.
    """
    if not username:
        return []
    
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    team_song_ids = get_songs_in_teams(user_teams)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT DISTINCT l.name 
    FROM lyricist l
    JOIN wrotelyrics wl ON l.name = wl.lyricist
    WHERE wl.song_id IN ({placeholders})
    ORDER BY l.name
    """
    
    cursor.execute(sql, team_song_ids)
    lyricists = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return lyricists


def get_all_songs_user_teams(username):
    """
    Returns all songs in teams in which the user participates.
    """
    if not username:
        return []
    
    user_teams = get_teams_of_user(username)
    if not user_teams:
        return []
    
    team_song_ids = get_songs_in_teams(user_teams)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT id, title, made_by
    FROM song
    WHERE id IN ({placeholders})
    ORDER BY title
    """
    
    cursor.execute(sql, team_song_ids)
    songs = []
    for row in cursor.fetchall():
        songs.append({
            'id': row[0],
            'title': row[1],
            'made_by': row[2]
        })
    cursor.close()
    
    return songs


def get_all_composers_specific_team(team_name):
    """
    Returns all composers that are in songs in the specified team.
    """
    if not team_name:
        return []
    
    team_song_ids = get_songs_in_specific_team(team_name)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT DISTINCT c.name 
    FROM composer c
    JOIN wrotemusic wm ON c.name = wm.composer
    WHERE wm.song_id IN ({placeholders})
    ORDER BY c.name
    """
    
    cursor.execute(sql, team_song_ids)
    composers = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return composers


def get_all_lyricists_specific_team(team_name):
    """
    Returns all lyricists that are in songs in the specified team.
    """
    if not team_name:
        return []
    
    team_song_ids = get_songs_in_specific_team(team_name)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT DISTINCT l.name 
    FROM lyricist l
    JOIN wrotelyrics wl ON l.name = wl.lyricist
    WHERE wl.song_id IN ({placeholders})
    ORDER BY l.name
    """
    
    cursor.execute(sql, team_song_ids)
    lyricists = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return lyricists


def get_all_songs_specific_team(team_name):
    """
    Returns all songs in the specified team.
    """
    if not team_name:
        return []
    
    team_song_ids = get_songs_in_specific_team(team_name)
    if not team_song_ids:
        return []
    
    db = get_db()
    cursor = db.cursor()
    
    placeholders = ','.join(['%s'] * len(team_song_ids))
    sql = f"""
    SELECT id, title, made_by
    FROM song
    WHERE id IN ({placeholders})
    ORDER BY title
    """
    
    cursor.execute(sql, team_song_ids)
    songs = []
    for row in cursor.fetchall():
        songs.append({
            'id': row[0],
            'title': row[1],
            'made_by': row[2]
        })
    cursor.close()
    
    return songs