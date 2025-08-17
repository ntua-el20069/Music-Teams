"""
Song access control utilities for Music Teams application.

This module contains helper functions to check user permissions
for song reading and writing operations based on team memberships.
"""

from typing import List, Tuple
from sqlalchemy.orm import Session

from backend.monolith.models.models import Song, MemberOfTeam, TeamsShareSongs


def song_exists_by_user(db: Session, user_id: int, title: str) -> Tuple[bool, str]:
    """
    Check if a song with the same title already exists made by the same user.
    
    Args:
        db: Database session
        user_id: ID of the user creating/updating the song
        title: Title of the song to check
        
    Returns:
        Tuple[bool, str]: (exists, message)
    """
    try:
        existing_song = db.query(Song).filter(
            Song.made_by == user_id,
            Song.title == title
        ).first()
        
        if existing_song:
            return (True, f"A song with title '{title}' already exists by this user")
        
        return (False, "Song title is available")
        
    except Exception as exc:
        print(f"Error checking song existence: {exc}")
        return (False, f"Error checking song existence: {exc}")


def can_write_song(db: Session, user_id: int, teams_sharing_song: List[str]) -> Tuple[bool, str]:
    """
    Check if user is enrolled in all teams that share the song and has can_edit = True.
    
    Args:
        db: Database session
        user_id: ID of the user
        teams_sharing_song: List of team names that will share the song
        
    Returns:
        Tuple[bool, str]: (can_write, message)
    """
    try:
        # If no teams specified, user can write (song is private or public only)
        if not teams_sharing_song:
            return (True, "No team restrictions")
        
        # Check each team
        for team_name in teams_sharing_song:
            membership = db.query(MemberOfTeam).filter(
                MemberOfTeam.user_id == user_id,
                MemberOfTeam.teamname == team_name
            ).first()
            
            if not membership:
                return (False, f"User is not enrolled in team '{team_name}'")
            
            if not membership.can_edit:
                return (False, f"User does not have edit permissions in team '{team_name}'")
        
        return (True, "User has write permissions for all specified teams")
        
    except Exception as exc:
        print(f"Error checking write permissions: {exc}")
        return (False, f"Error checking write permissions: {exc}")


def can_read_song(db: Session, user_id: int, teams_sharing_song: List[str]) -> Tuple[bool, str]:
    """
    Check if user is enrolled in at least one team that shares the song.
    
    Args:
        db: Database session
        user_id: ID of the user
        teams_sharing_song: List of team names that share the song
        
    Returns:
        Tuple[bool, str]: (can_read, message)
    """
    try:
        # If no teams specified, assume public access or check other logic
        if not teams_sharing_song:
            return (True, "No team restrictions")
        
        # Check if user is enrolled in at least one team
        for team_name in teams_sharing_song:
            membership = db.query(MemberOfTeam).filter(
                MemberOfTeam.user_id == user_id,
                MemberOfTeam.teamname == team_name
            ).first()
            
            if membership:
                return (True, f"User has access through team '{team_name}'")
        
        return (False, "User is not enrolled in any of the teams that share this song")
        
    except Exception as exc:
        print(f"Error checking read permissions: {exc}")
        return (False, f"Error checking read permissions: {exc}")