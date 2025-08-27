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
