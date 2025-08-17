from typing import Dict, List, Tuple

from sqlalchemy import distinct
from sqlalchemy import exc as sqlalchemy_exc
from sqlalchemy.orm import Session

from backend.monolith.models.models import (
    MemberOfTeam,
    Song,
    Team,
    TeamsShareSongs,
    WroteLyrics,
    WroteMusic,
)


def get_all_public_composers(db: Session) -> Tuple[bool, str, List[str]]:
    """
    Get all composers that are in public songs.

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of composer names
    """
    try:
        composers = (
            db.query(distinct(WroteMusic.composer))
            .join(Song, WroteMusic.song_id == Song.id)
            .filter(Song.public == True)  # noqa: E712
            .all()
        )

        composer_names = [composer[0] for composer in composers]
        return True, "Public composers retrieved successfully", composer_names

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_public_composers: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_public_composers: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_public_lyricists(db: Session) -> Tuple[bool, str, List[str]]:
    """
    Get all lyricists that are in public songs.

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of lyricist names
    """
    try:
        lyricists = (
            db.query(distinct(WroteLyrics.lyricist))
            .join(Song, WroteLyrics.song_id == Song.id)
            .filter(Song.public == True)  # noqa: E712
            .all()
        )

        lyricist_names = [lyricist[0] for lyricist in lyricists]
        return True, "Public lyricists retrieved successfully", lyricist_names

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_public_lyricists: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_public_lyricists: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_public_songs(db: Session) -> Tuple[bool, str, List[Dict[str, str]]]:
    """
    Get all public songs.

    Returns:
        Tuple[bool, str, List[Dict[str, str]]]: Success status, message,
            list of song dictionaries with id and title
    """
    try:
        songs = (
            db.query(Song.id, Song.title)
            .filter(Song.public == True)  # noqa: E712
            .all()
        )

        song_list = [{"id": str(song[0]), "title": song[1]} for song in songs]
        return True, "Public songs retrieved successfully", song_list

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_public_songs: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_public_songs: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_composers_in_user_teams(
    db: Session, user_id: int
) -> Tuple[bool, str, List[str]]:
    """
    Get all composers that are in songs in teams the user participates in.

    Args:
        db: Database session
        user_id: ID of the user

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of composer names
    """
    try:
        composers = (
            db.query(distinct(WroteMusic.composer))
            .join(Song, WroteMusic.song_id == Song.id)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .join(Team, TeamsShareSongs.teamname == Team.name)
            .join(MemberOfTeam, Team.name == MemberOfTeam.teamname)
            .filter(MemberOfTeam.user_id == user_id)
            .all()
        )

        composer_names = [composer[0] for composer in composers]
        return True, "Composers in user teams retrieved successfully", composer_names

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_composers_in_user_teams: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_composers_in_user_teams: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_lyricists_in_user_teams(
    db: Session, user_id: int
) -> Tuple[bool, str, List[str]]:
    """
    Get all lyricists that are in songs in teams the user participates in.

    Args:
        db: Database session
        user_id: ID of the user

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of lyricist names
    """
    try:
        lyricists = (
            db.query(distinct(WroteLyrics.lyricist))
            .join(Song, WroteLyrics.song_id == Song.id)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .join(Team, TeamsShareSongs.teamname == Team.name)
            .join(MemberOfTeam, Team.name == MemberOfTeam.teamname)
            .filter(MemberOfTeam.user_id == user_id)
            .all()
        )

        lyricist_names = [lyricist[0] for lyricist in lyricists]
        return True, "Lyricists in user teams retrieved successfully", lyricist_names

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_lyricists_in_user_teams: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_lyricists_in_user_teams: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_songs_in_user_teams(
    db: Session, user_id: int
) -> Tuple[bool, str, List[Dict[str, str]]]:
    """
    Get all songs in teams the user participates in.

    Args:
        db: Database session
        user_id: ID of the user

    Returns:
        Tuple[bool, str, List[Dict[str, str]]]: Success status, message,
            list of song dictionaries with id and title
    """
    try:
        songs = (
            db.query(Song.id, Song.title)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .join(Team, TeamsShareSongs.teamname == Team.name)
            .join(MemberOfTeam, Team.name == MemberOfTeam.teamname)
            .filter(MemberOfTeam.user_id == user_id)
            .distinct()
            .all()
        )

        song_list = [{"id": str(song[0]), "title": song[1]} for song in songs]
        return True, "Songs in user teams retrieved successfully", song_list

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_songs_in_user_teams: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_songs_in_user_teams: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_composers_in_team(
    db: Session, team_name: str
) -> Tuple[bool, str, List[str]]:
    """
    Get all composers that are in songs in a specific team.

    Args:
        db: Database session
        team_name: Name of the team

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of composer names
    """
    try:
        composers = (
            db.query(distinct(WroteMusic.composer))
            .join(Song, WroteMusic.song_id == Song.id)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .filter(TeamsShareSongs.teamname == team_name)
            .all()
        )

        composer_names = [composer[0] for composer in composers]
        return (
            True,
            f"Composers in team {team_name} retrieved successfully",
            composer_names,
        )

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_composers_in_team: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_composers_in_team: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_lyricists_in_team(
    db: Session, team_name: str
) -> Tuple[bool, str, List[str]]:
    """
    Get all lyricists that are in songs in a specific team.

    Args:
        db: Database session
        team_name: Name of the team

    Returns:
        Tuple[bool, str, List[str]]: Success status, message, list of lyricist names
    """
    try:
        lyricists = (
            db.query(distinct(WroteLyrics.lyricist))
            .join(Song, WroteLyrics.song_id == Song.id)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .filter(TeamsShareSongs.teamname == team_name)
            .all()
        )

        lyricist_names = [lyricist[0] for lyricist in lyricists]
        return (
            True,
            f"Lyricists in team {team_name} retrieved successfully",
            lyricist_names,
        )

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_lyricists_in_team: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_lyricists_in_team: {exc}")
        return False, f"Unexpected error: {exc}", []


def get_all_songs_in_team(
    db: Session, team_name: str
) -> Tuple[bool, str, List[Dict[str, str]]]:
    """
    Get all songs in a specific team.

    Args:
        db: Database session
        team_name: Name of the team

    Returns:
        Tuple[bool, str, List[Dict[str, str]]]: Success status, message,
            list of song dictionaries with id and title
    """
    try:
        songs = (
            db.query(Song.id, Song.title)
            .join(TeamsShareSongs, Song.id == TeamsShareSongs.song_id)
            .filter(TeamsShareSongs.teamname == team_name)
            .distinct()
            .all()
        )

        song_list = [{"id": str(song[0]), "title": song[1]} for song in songs]
        return True, f"Songs in team {team_name} retrieved successfully", song_list

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(f"Database error in get_all_songs_in_team: {exc}")
        return False, f"Database error: {exc}", []
    except Exception as exc:
        print(f"Unexpected error in get_all_songs_in_team: {exc}")
        return False, f"Unexpected error: {exc}", []
