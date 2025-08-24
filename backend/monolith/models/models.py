import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from backend.monolith.database.database import db_type_url

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

DB_USERSNAME = str(os.getenv("DB_USERNAME"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_DATABASE = str(os.getenv("DB_DATABASE"))

Base = declarative_base()  # type: ignore


class User(Base):  # type: ignore
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    role = Column(String(20), nullable=False)  # TODO: enum
    registered_with_google = Column(Boolean, default=False)
    # verification_token = Column(String(50), nullable=True)
    # verified = Column(Boolean, default=False)

    # Relationships
    songs = relationship("Song", backref="creator")
    team_memberships = relationship("MemberOfTeam", backref="user")
    active_sessions = relationship("ActiveSession", backref="user")


class UserModel(BaseModel):
    id: int = Field(default=None, title="User ID")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    email: str = Field(default=None, title="Email")
    role: str = Field(..., title="Role")
    registered_with_google: bool = Field(default=False, title="Registered with Google")
    # verified: bool = Field(default=False, title="Verified")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "username": "my_username",
                "password": "my_password",
                "email": "my_email@gmail.com",
                "role": "user",
                "registered_with_google": True,
                # "verified": False,
            }
        }


class UserUpdateModel(BaseModel):
    username: str
    password: str


class UserManualLoginModel(BaseModel):
    username: str
    password: str


class ActiveSession(Base):  # type: ignore
    __tablename__ = "active_session"

    # token = Column(String(50), primary_key=True)
    session_id = Column(String(50), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_email = Column(String(80))
    username = Column(String(20))
    role = Column(String(20))  # user's role at session creation
    expires_at = Column(DateTime, nullable=False)


class ActiveSessionModel(BaseModel):
    # token: str = Field(..., title="ActiveSession Token")
    session_id: str = Field(..., title="ActiveSession ID")
    user_id: int = Field(..., title="User ID")
    user_email: str = Field(..., title="User Email")
    username: str = Field(..., title="Username")
    role: str = Field(..., title="Role")
    expires_at: str = Field(
        ..., title="Expiration Time", description="ISO format datetime string"
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "session_id": "abc123xyz",
                "user_id": 1,
                "user_email": "my_mail@gmail.com",
                "username": "AntonisNikos",
                "role": "user",
                "expires_at": "2023-10-01T12:00:00Z",
            }
        }


class Song(Base):  # type: ignore
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    lyrics = Column(Text)
    chords = Column(Text, default="")
    likes = Column(Integer, default=0)
    made_by = Column(Integer, ForeignKey("user.id"))
    public = Column(Boolean, default=False)

    # Relationships
    composers = relationship("Composer", secondary="wrotemusic", back_populates="songs")
    lyricists = relationship(
        "Lyricist", secondary="wrotelyrics", back_populates="songs"
    )
    shared_with_teams = relationship(
        "Team", secondary="teams_share_songs", back_populates="shared_songs"
    )


class SimpleSongModel(BaseModel):
    id: int = Field(default=None, title="Song ID")
    title: str = Field(..., title="Song Title")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Song Title",
            }
        }


class SongModel(BaseModel):
    id: int = Field(default=None, title="Song ID")
    title: str = Field(..., title="Song Title")
    lyrics: str = Field(..., title="Song Lyrics")
    chords: str = Field(default="", title="Song Chords")
    likes: int = Field(default=0, title="Likes")
    made_by: int = Field(
        title="Made By (user id)",
    )
    public: bool = Field(default=False, title="Public")
    composers: list[str] = Field(default=[], title="Composers")
    lyricists: list[str] = Field(default=[], title="Lyricists")
    shared_with_teams: list[str] = Field(
        default=[],
        title="Shared With Teams",
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Song Title",
                "lyrics": "These are the lyrics of the song.",
                "chords": "C G Am F",
                "likes": 10,
                "made_by": 1,
                "public": True,
                "composers": ["Composer1", "Composer2"],
                "lyricists": ["Lyricist1", "Lyricist2"],
                "shared_with_teams": ["Team1", "Team2"],
            }
        }


class UpdateLyricsChordsModel(BaseModel):
    song_id: int = Field(..., title="Song ID")
    lyrics: str = Field(..., title="Song Lyrics")
    chords: str = Field(..., title="Song Chords")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "song_id": 1,
                "lyrics": "These are the updated lyrics of the song.",
                "chords": "C G Am F",
            }
        }


class UpdateChordsModel(BaseModel):
    song_id: int = Field(
        ..., title="Song ID", description="Unique identifier for the song"
    )
    chords: str = Field(..., title="Song Chords")

    class Config:
        orm_mode = True
        schema_extra = {"example": {"song_id": 1, "chords": "C G Am F"}}


class SongInsertModel(BaseModel):
    """Model for song insertion requests."""

    title: str = Field(..., title="Song Title")
    composers: list[str] = Field(default=[], title="Composers")
    lyricists: list[str] = Field(default=[], title="Lyricists")
    lyrics: str = Field(..., title="Song Lyrics")
    public: bool = Field(default=False, title="Public")
    shared_with_teams: list[str] = Field(default=[], title="Shared With Teams")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "My Song",
                "composers": ["Composer1", "Composer2"],
                "lyricists": ["Lyricist1"],
                "lyrics": "These are the song lyrics",
                "public": False,
                "shared_with_teams": ["Team1", "Team2"],
            }
        }


class SongUpdateModel(BaseModel):
    """Model for song update requests."""

    id: int = Field(..., title="Song ID")
    title: str = Field(..., title="Song Title")
    composers: list[str] = Field(default=[], title="Composers")
    lyricists: list[str] = Field(default=[], title="Lyricists")
    lyrics: str = Field(..., title="Song Lyrics")
    public: bool = Field(default=False, title="Public")
    shared_with_teams: list[str] = Field(default=[], title="Shared With Teams")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Updated Song Title",
                "composers": ["Composer1", "Composer2"],
                "lyricists": ["Lyricist1"],
                "lyrics": "These are the updated song lyrics",
                "public": True,
                "shared_with_teams": ["Team1"],
            }
        }


class TransportoModel(BaseModel):
    """Model for permanent transposition requests."""

    song_id: int = Field(..., title="Song ID")
    transporto_units: int = Field(..., title="Transposition Units")

    class Config:
        orm_mode = True
        schema_extra = {"example": {"song_id": 1, "transporto_units": 2}}


class Composer(Base):  # type: ignore
    __tablename__ = "composer"

    name = Column(String(50), primary_key=True)

    # Relationships
    songs = relationship("Song", secondary="wrotemusic", back_populates="composers")


class Lyricist(Base):  # type: ignore
    __tablename__ = "lyricist"

    name = Column(String(50), primary_key=True)

    # Relationships
    songs = relationship("Song", secondary="wrotelyrics", back_populates="lyricists")


class WroteMusic(Base):  # type: ignore
    __tablename__ = "wrotemusic"

    composer = Column(String(50), ForeignKey("composer.name"), primary_key=True)
    song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)


class WroteLyrics(Base):  # type: ignore
    __tablename__ = "wrotelyrics"

    lyricist = Column(String(50), ForeignKey("lyricist.name"), primary_key=True)
    song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)


class Team(Base):  # type: ignore
    __tablename__ = "team"

    name = Column(String(50), primary_key=True)
    team_id = Column(String(50), unique=True, nullable=False)

    # Relationships
    members = relationship("MemberOfTeam", backref="team")
    shared_songs = relationship(
        "Song", secondary="teams_share_songs", back_populates="shared_with_teams"
    )


class TeamModel(BaseModel):
    team_name: str
    team_id: str


class TeamCodeModel(BaseModel):
    team_code: str


class MemberOfTeam(Base):  # type: ignore
    __tablename__ = "member_of_team"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    teamname = Column(
        String(50), ForeignKey("team.name"), primary_key=True, default="NTUA"
    )
    points = Column(Integer, default=0)
    can_edit = Column(Boolean, default=True)


class TeamsShareSongs(Base):  # type: ignore
    __tablename__ = "teams_share_songs"

    teamname = Column(String(50), ForeignKey("team.name"), primary_key=True)
    song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)


# Create engine
DB_TYPE, DATABASE_URL = db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
