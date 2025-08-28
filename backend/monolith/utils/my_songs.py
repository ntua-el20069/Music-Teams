"""
My Songs utilities for Music Teams application.

This module contains helper functions to retrieve songs, composers, and lyricists
for songs created by a specific user.
"""

from typing import Dict, List, Tuple

from sqlalchemy.orm import Session

from backend.monolith.models.models import Song, WroteLyrics, WroteMusic


def get_user_songs(db: Session, user_id: int) -> Tuple[bool, str, List[Dict[str, str]]]:
    """
    Get all songs created by a specific user.

    Args:
        db: Database session
        user_id: ID of the user whose songs to retrieve

    Returns:
        Tuple[bool, str, List[Dict[str,str]]]: (success, message, songs_list)
    """
    try:
        # Get all songs made by this user
        songs = db.query(Song).filter(Song.made_by == user_id).all()

        songs_dicts = [{"id": str(song.id), "title": song.title} for song in songs]

        return (True, f"Found {len(songs_dicts)} songs", songs_dicts)

    except Exception as exc:
        print(f"Error getting user songs: {exc}")
        return (False, f"Error getting user songs: {exc}", [])


def get_user_composers(db: Session, user_id: int) -> Tuple[bool, str, List[str]]:
    """
    Get all unique composers from songs created by a specific user.

    Args:
        db: Database session
        user_id: ID of the user whose composers to retrieve

    Returns:
        Tuple[bool, str, List[str]]: (success, message, composers_list)
    """
    try:
        # Get all unique composers from songs made by this user
        composers = (
            db.query(WroteMusic.composer)
            .join(Song, WroteMusic.song_id == Song.id)
            .filter(Song.made_by == user_id)
            .distinct()
            .all()
        )

        composer_names = [composer[0] for composer in composers]

        return (True, f"Found {len(composer_names)} unique composers", composer_names)

    except Exception as exc:
        print(f"Error getting user composers: {exc}")
        return (False, f"Error getting user composers: {exc}", [])


def get_user_lyricists(db: Session, user_id: int) -> Tuple[bool, str, List[str]]:
    """
    Get all unique lyricists from songs created by a specific user.

    Args:
        db: Database session
        user_id: ID of the user whose lyricists to retrieve

    Returns:
        Tuple[bool, str, List[str]]: (success, message, lyricists_list)
    """
    try:
        # Get all unique lyricists from songs made by this user
        lyricists = (
            db.query(WroteLyrics.lyricist)
            .join(Song, WroteLyrics.song_id == Song.id)
            .filter(Song.made_by == user_id)
            .distinct()
            .all()
        )

        lyricist_names = [lyricist[0] for lyricist in lyricists]

        return (True, f"Found {len(lyricist_names)} unique lyricists", lyricist_names)

    except Exception as exc:
        print(f"Error getting user lyricists: {exc}")
        return (False, f"Error getting user lyricists: {exc}", [])
