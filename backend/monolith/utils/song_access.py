"""
Song access control utilities for Music Teams application.

This module contains helper functions to check user permissions
for song reading and writing operations based on team memberships.
"""

from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from backend.monolith.models.models import (
    MemberOfTeam,
    Song,
    SongModel,
    TeamsShareSongs,
    WroteLyrics,
    WroteMusic,
)


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
        existing_song = (
            db.query(Song).filter(Song.made_by == user_id, Song.title == title).first()
        )

        if existing_song:
            return (True, f"A song with title '{title}' already exists by this user")

        return (False, "Song title is available")

    except Exception as exc:
        print(f"Error checking song existence: {exc}")
        return (False, f"Error checking song existence: {exc}")


def can_write_song(
    db: Session, user_id: int, teams_sharing_song: List[str]
) -> Tuple[bool, str]:
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
            membership = (
                db.query(MemberOfTeam)
                .filter(
                    MemberOfTeam.user_id == user_id, MemberOfTeam.teamname == team_name
                )
                .first()
            )

            if not membership:
                return (False, f"User is not enrolled in team '{team_name}'")

            if not membership.can_edit:
                return (
                    False,
                    f"User does not have edit permissions in team '{team_name}'",
                )

        return (True, "User has write permissions for all specified teams")

    except Exception as exc:
        print(f"Error checking write permissions: {exc}")
        return (False, f"Error checking write permissions: {exc}")


def can_read_song(db: Session, user_id: int, song_id: int) -> Tuple[bool, str]:
    """
    Check if user can read a song based on ownership, public status, or team membership.

    Args:
        db: Database session
        user_id: ID of the user
        song_id: ID of the song to check access for

    Returns:
        Tuple[bool, str]: (can_read, message)
    """
    try:
        # Get the song
        song = db.query(Song).filter(Song.id == song_id).first()
        if not song:
            return (False, f"Song with ID {song_id} not found")

        # Check if song is public or user owns it
        if not song.public and song.made_by != user_id:
            # Get teams that share this song
            teams_query = (
                db.query(TeamsShareSongs)
                .filter(TeamsShareSongs.song_id == song_id)
                .all()
            )
            teams_sharing_song = [ts.teamname for ts in teams_query]

            # If no teams specified, user cannot read private song they don't own
            if not teams_sharing_song:
                return (False, "Song is private and you are not the owner")

            # Check if user is enrolled in at least one team
            for team_name in teams_sharing_song:
                membership = (
                    db.query(MemberOfTeam)
                    .filter(
                        MemberOfTeam.user_id == user_id,
                        MemberOfTeam.teamname == team_name,
                    )
                    .first()
                )

                if membership:
                    return (True, f"User has access through team '{team_name}'")

            return (
                False,
                "User is not enrolled in any of the teams that share this song",
            )

        # Song is public or user owns it
        return (True, "User has access to the song")

    except Exception as exc:
        print(f"Error checking read permissions: {exc}")
        return (False, f"Error checking read permissions: {exc}")


def get_song_by_id_with_ownership(
    db: Session, song_id: int, user_id: int
) -> Tuple[Optional[SongModel], str]:
    """
    Get a song by ID and check if the user owns it.

    Args:
        db: Database session
        song_id: ID of the song to retrieve
        user_id: ID of the user to check ownership for

    Returns:
        Tuple[Optional[SongModel], str]: (song or None, message)
    """
    try:
        song = db.query(Song).filter(Song.id == song_id).first()

        if not song:
            return (None, f"Song with ID {song_id} not found")

        if song.made_by != user_id:
            return (None, "You can only update songs that you created")

        song_model_instance = SongModel(
            id=song.id,
            title=song.title,
            chords=song.chords,
            lyrics=song.lyrics,
            likes=song.likes,
            made_by=song.made_by,
            public=song.public,
            composers=[
                cm[0]
                for cm in db.query(WroteMusic.composer)
                .filter(WroteMusic.song_id == song_id)
                .all()
            ],
            lyricists=[
                ly[0]
                for ly in db.query(WroteLyrics.lyricist)
                .filter(WroteLyrics.song_id == song_id)
                .all()
            ],
            shared_with_teams=[
                share.teamname
                for share in db.query(TeamsShareSongs)
                .filter(TeamsShareSongs.song_id == song_id)
                .all()
            ],
        )
        # Currently, composers, lyricists, and shared_with_teams are not needed.
        # only title and chords are used in update operations.
        return (song_model_instance, "Song found and ownership verified")

    except Exception as exc:
        print(f"Error getting song by ID with ownership: {exc}")
        return (None, f"Error getting song by ID with ownership: {exc}")


def delete_song_by_id(db: Session, song_id: int, user_id: int) -> Tuple[bool, str]:
    """
    Delete a song by ID with proper foreign key constraint handling.
    
    Only the user who created the song (made_by field) can delete it.
    Deletes in order to respect foreign key constraints:
    1. TeamsShareSongs records
    2. WroteMusic records  
    3. WroteLyrics records
    4. Song itself
    
    Args:
        db: Database session
        song_id: ID of the song to delete
        user_id: ID of the user requesting deletion
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        # First check if song exists and user owns it
        song = db.query(Song).filter(Song.id == song_id).first()
        
        if not song:
            return (False, f"Song with ID {song_id} not found")
            
        if song.made_by != user_id:
            return (False, "You can only delete songs that you created")
        
        # Delete related records first due to foreign key constraints
        
        # 1. Delete team sharing relationships
        deleted_teams = db.query(TeamsShareSongs).filter(
            TeamsShareSongs.song_id == song_id
        ).delete()
        
        # 2. Delete composer relationships
        deleted_composers = db.query(WroteMusic).filter(
            WroteMusic.song_id == song_id
        ).delete()
        
        # 3. Delete lyricist relationships
        deleted_lyricists = db.query(WroteLyrics).filter(
            WroteLyrics.song_id == song_id
        ).delete()
        
        # 4. Finally delete the song itself
        db.delete(song)
        
        # Commit all changes
        db.commit()
        
        return (True, f"Song '{song.title}' deleted successfully (removed {deleted_teams} team shares, {deleted_composers} composer relations, {deleted_lyricists} lyricist relations)")
        
    except Exception as exc:
        db.rollback()
        print(f"Error deleting song: {exc}")
        return (False, f"Error deleting song: {exc}")
