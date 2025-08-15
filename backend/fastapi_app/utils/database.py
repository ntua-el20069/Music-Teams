"""
Database utilities for FastAPI application.
Adapted from backend/__init__.py to work with FastAPI.
"""

import mysql.connector
from typing import List
import os
import sys

# Add parent directory to path to import from backend
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Configuration
mode = 'local'  # CHANGE: mode = 'local' for local PC database, mode = 'web' for PythonAnywhere Database


def get_db_connection():
    """
    Get database connection.
    Adapted from backend/__init__.py get_db() function.
    """
    db_name = "songs" if mode == 'local' else "nikolaospapa3$musicteams"
    
    # for MySQL
    if mode == 'local':
        db = mysql.connector.connect(
            port=3307,
            host="localhost",
            user="root",
            password="",  # change it for your DBMS
            database=db_name,
            charset="utf8",
            use_unicode=True
        )
    else:
        db = mysql.connector.connect(
            host="nikolaospapa3.mysql.pythonanywhere-services.com",
            user="nikolaospapa3",
            password="",  # CHANGE: change it for your DBMS
            database=db_name,
            charset="utf8",
            use_unicode=True
        )
    
    cursor = db.cursor()
    cursor.execute("SET NAMES utf8;")
    cursor.execute("SET CHARACTER SET utf8;")
    cursor.execute("SET character_set_connection = utf8;")
    
    return db


def get_all_composers() -> List[str]:
    """
    Get all composers from the database.
    Based on backend/all.py all_composers() function.
    """
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql = "SELECT name FROM composer"
        cursor.execute(sql)
        composers = [x[0] for x in cursor.fetchall()]
        return composers
    finally:
        db.close()


def get_all_lyricists() -> List[str]:
    """
    Get all lyricists from the database.
    Based on backend/all.py all_lyricists() function.
    """
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql = "SELECT name FROM lyricist"
        cursor.execute(sql)
        lyricists = [x[0] for x in cursor.fetchall()]
        return lyricists
    finally:
        db.close()


def get_all_songs() -> List[str]:
    """
    Get all songs from the database.
    Based on backend/all.py all_songs() function.
    """
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql = "SELECT title FROM song"
        cursor.execute(sql)
        songs = [x[0] for x in cursor.fetchall()]
        return songs
    finally:
        db.close()


def get_public_composers() -> List[str]:
    """
    Get composers from public songs only.
    """
    db = get_db_connection()
    try:
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
        return composers
    finally:
        db.close()


def get_public_lyricists() -> List[str]:
    """
    Get lyricists from public songs only.
    """
    db = get_db_connection()
    try:
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
        return lyricists
    finally:
        db.close()


def get_public_songs() -> List[str]:
    """
    Get public songs only.
    """
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql = "SELECT title FROM song WHERE public = 1 ORDER BY title"
        cursor.execute(sql)
        songs = [x[0] for x in cursor.fetchall()]
        return songs
    finally:
        db.close()


# Placeholder functions for team-related queries
# TODO: Implement these when team tables are available

def get_teams_of_user(user_id: str) -> List[str]:
    """
    Get teams that a user belongs to.
    TODO: Implement when team tables are created.
    
    Expected SQL:
    SELECT team_name FROM team_members WHERE user_id = %s
    """
    # Placeholder implementation
    return ["team1", "team2"]  # Mock data for now


def get_myteams_composers(user_id: str) -> List[str]:
    """
    Get composers from songs of user's teams.
    TODO: Implement when team tables are created.
    
    Expected SQL:
    SELECT DISTINCT c.name 
    FROM composer c 
    JOIN wrotemusic wm ON c.name = wm.composer 
    JOIN song s ON wm.song_id = s.id 
    JOIN team_songs ts ON s.id = ts.song_id 
    JOIN team_members tm ON ts.team_name = tm.team_name 
    WHERE tm.user_id = %s
    ORDER BY c.name
    """
    # Placeholder implementation
    return ["Team Composer 1", "Team Composer 2"]


def get_myteams_lyricists(user_id: str) -> List[str]:
    """
    Get lyricists from songs of user's teams.
    TODO: Implement when team tables are created.
    """
    # Placeholder implementation
    return ["Team Lyricist 1", "Team Lyricist 2"]


def get_myteams_songs(user_id: str) -> List[str]:
    """
    Get songs from user's teams.
    TODO: Implement when team tables are created.
    """
    # Placeholder implementation
    return ["Team Song 1", "Team Song 2"]


def get_team_composers(team_name: str) -> List[str]:
    """
    Get composers from specific team's songs.
    TODO: Implement when team tables are created.
    """
    # Placeholder implementation
    return [f"{team_name} Composer 1", f"{team_name} Composer 2"]


def get_team_lyricists(team_name: str) -> List[str]:
    """
    Get lyricists from specific team's songs.
    TODO: Implement when team tables are created.
    """
    # Placeholder implementation
    return [f"{team_name} Lyricist 1", f"{team_name} Lyricist 2"]


def get_team_songs(team_name: str) -> List[str]:
    """
    Get songs from specific team.
    TODO: Implement when team tables are created.
    """
    # Placeholder implementation
    return [f"{team_name} Song 1", f"{team_name} Song 2"]