"""
Song creation and update utilities for Music Teams application.

This module contains functions for creating, updating songs and managing
composers, lyricists, and team sharing relationships.
"""

from typing import List, Optional, Tuple

from sqlalchemy import exc as sqlalchemy_exc
from sqlalchemy.orm import Session

from backend.monolith.models.models import (
    Composer,
    Lyricist,
    Song,
    SongModel,
    Team,
    TeamsShareSongs,
    WroteLyrics,
    WroteMusic,
)

major = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

sharp_to_flat = {"C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb"}
flat_to_sharp = {v: k for k, v in sharp_to_flat.items()}


def transpose_chords(chords: str, transporto: int) -> str:
    """
    Transpose a single chord by the specified number of semitones.

    Args:
        chord: The chord to transpose (e.g., "C", "Am", "F#")
        semitones: Number of semitones to transpose (positive = up, negative = down)

    Returns:
        str: The transposed chord
    """
    # Replace all flats with their sharp equivalents in the chords string
    for flat, sharp in flat_to_sharp.items():
        chords = chords.replace(flat, sharp)

    transposed_chords = ""
    i = 0
    while i < len(chords):  # for each letter in chords string
        if chords[i : i + 2] in major:  # check if it is A#, C#, ... # noqa: E203
            k = major.index(chords[i : i + 2])  # noqa: E203
            transposed_chords += major[(k + transporto) % 12]
            i += 2
        elif chords[i] in major:  # check if it is A, B, C, ...
            k = major.index(chords[i])
            transposed_chords += major[(k + transporto) % 12]
            i += 1
        else:  # else write the same character
            transposed_chords += chords[i]
            i += 1
    return transposed_chords


def manage_song(
    db: Session,
    song_model: SongModel,
    update_chords: bool = False,
    update_song: bool = False,
) -> Tuple[bool, str, Optional[int]]:
    """
    Main function to manage song creation and updates.

    Args:
        db: Database session
        song_model: SongModel instance with song data
        update_chords: If True, update chords in the database
        update_song: If True, update existing song; if False, insert new song

    Returns:
        Tuple[bool, str, Optional[int]]: (success, message, song_id)
    """
    try:

        if update_song:
            # Update existing song
            if not song_model.id:
                return (False, "Song ID is required for updates", None)

            song = db.query(Song).filter(Song.id == song_model.id).first()
            if not song:
                return (False, f"Song with ID {song_model.id} not found", None)

            # Update song fields
            song.title = song_model.title
            song.lyrics = song_model.lyrics
            song.public = song_model.public

            if update_chords:
                song.chords = song_model.chords

            song_id = song.id

        else:
            # Insert new song
            new_song = Song(
                title=song_model.title,
                lyrics=song_model.lyrics,
                chords=song_model.chords if update_chords else "",
                made_by=song_model.made_by,
                public=song_model.public,
            )

            db.add(new_song)
            db.flush()  # Get the ID without committing
            song_id = new_song.id

        # Handle composers and lyricists
        if update_song:
            # Delete existing relationships for updates
            db.query(WroteMusic).filter(WroteMusic.song_id == song_id).delete()
            db.query(WroteLyrics).filter(WroteLyrics.song_id == song_id).delete()

        # Insert composers
        for composer_name in song_model.composers:
            if composer_name.strip():
                # Insert composer if not exists
                composer = (
                    db.query(Composer).filter(Composer.name == composer_name).first()
                )
                if not composer:
                    composer = Composer(name=composer_name)
                    db.add(composer)

                # Create relationship
                wrote_music = WroteMusic(composer=composer_name, song_id=song_id)
                db.add(wrote_music)

        # Insert lyricists
        for lyricist_name in song_model.lyricists:
            if lyricist_name.strip():
                # Insert lyricist if not exists
                lyricist = (
                    db.query(Lyricist).filter(Lyricist.name == lyricist_name).first()
                )
                if not lyricist:
                    lyricist = Lyricist(name=lyricist_name)
                    db.add(lyricist)

                # Create relationship
                wrote_lyrics = WroteLyrics(lyricist=lyricist_name, song_id=song_id)
                db.add(wrote_lyrics)

        # Handle team sharing
        if update_song:
            # Delete existing team sharing relationships
            db.query(TeamsShareSongs).filter(
                TeamsShareSongs.song_id == song_id
            ).delete()

        # Insert new team sharing relationships
        for team_name in song_model.shared_with_teams:
            if team_name.strip():
                # Verify team exists
                team = db.query(Team).filter(Team.name == team_name).first()
                if team:
                    team_share = TeamsShareSongs(teamname=team_name, song_id=song_id)
                    db.add(team_share)
                else:
                    db.rollback()
                    return (False, f"Team '{team_name}' does not exist", None)

        db.commit()

        action = "updated" if update_song else "created"
        return (True, f"Song {action} successfully", song_id)

    except sqlalchemy_exc.IntegrityError as exc:
        db.rollback()
        print(f"Database integrity error: {exc}")
        return (False, f"Database integrity error: {exc}", None)

    except Exception as exc:
        db.rollback()
        print(f"Unexpected error during song management: {exc}")
        return (False, f"Unexpected error: {exc}", None)


def get_song_with_teams(
    db: Session, song_id: int
) -> Tuple[Optional[SongModel], List[str]]:
    """
    Get a song and the list of teams it's shared with.

    Args:
        db: Database session
        song_id: ID of the song

    Returns:
        Tuple[Optional[SongModel], List[str]]: (song, list of team names)
    """
    try:
        song = db.query(Song).filter(Song.id == song_id).first()
        if not song:
            return (None, [])

        # Get teams the song is shared with
        team_shares = (
            db.query(TeamsShareSongs).filter(TeamsShareSongs.song_id == song_id).all()
        )

        team_names = [share.teamname for share in team_shares]

        song_model_instance = SongModel(
            id=song.id,
            title=song.title,
            lyrics=song.lyrics,
            chords=song.chords,
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
            shared_with_teams=team_names,
        )
        return (song_model_instance, team_names)

    except Exception as exc:
        print(f"Error getting song with teams: {exc}")
        return (None, [])


def update_song_chords_only(
    db: Session, song_id: int, new_chords: str
) -> Tuple[bool, str]:
    """
    Update only the chords field of a song.

    Args:
        db: Database session
        song_id: ID of the song to update
        new_chords: New chords string

    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        song = db.query(Song).filter(Song.id == song_id).first()
        if not song:
            return (False, f"Song with ID {song_id} not found")

        song.chords = new_chords
        db.commit()

        return (True, "Song chords updated successfully")

    except Exception as exc:
        db.rollback()
        print(f"Error updating song chords: {exc}")
        return (False, f"Error updating song chords: {exc}")


def update_song_lyrics_chords(
    db: Session, song_id: int, new_lyrics: str, new_chords: str
) -> Tuple[bool, str]:
    """
    Update both lyrics and chords fields of a song.

    Args:
        db: Database session
        song_id: ID of the song to update
        new_lyrics: New lyrics string
        new_chords: New chords string

    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        song = db.query(Song).filter(Song.id == song_id).first()
        if not song:
            return (False, f"Song with ID {song_id} not found")

        song.lyrics = new_lyrics
        song.chords = new_chords
        db.commit()

        return (True, "Song lyrics and chords updated successfully")

    except Exception as exc:
        db.rollback()
        print(f"Error updating song lyrics and chords: {exc}")
        return (False, f"Error updating song lyrics and chords: {exc}")
