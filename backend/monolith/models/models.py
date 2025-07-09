from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from pydantic import BaseModel, Field

from dotenv import load_dotenv
import os
from backend.monolith.database.database import db_type_url

env_path = '.env'
load_dotenv(dotenv_path=env_path)

DB_USERSNAME = str(os.getenv('DB_USERNAME'))
DB_PASSWORD = str(os.getenv('DB_PASSWORD'))
DB_HOST = str(os.getenv('DB_HOST'))
DB_DATABASE = str(os.getenv('DB_DATABASE'))

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    username = Column(String(20), primary_key=True)
    password = Column(String(20))
    email = Column(String(80))
    role = Column(String(20))  # Will use UserRole enum for validation

    # Relationships
    songs = relationship("Song", backref="creator")
    team_memberships = relationship("MemberOfTeam", backref="user")
    active_sessions = relationship("ActiveSession", backref="user")

class ActiveSession(Base):
    __tablename__ = 'active_session'

    token = Column(String(50), primary_key=True)
    username = Column(String(20), ForeignKey('user.username'))
    role = Column(String(20))  # Mirrors user's role at session creation time

class ActiveSessionModel(BaseModel):
    token: str = Field(..., title="ActiveSession Token", description="Unique session token")
    username: str = Field(..., title="Username", description="Username of the user")
    role: str = Field(..., title="Role", description="Role of the user at session creation time")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "token": "abc123xyz",
                "username": "AntonisNikos",
                "role": "user"
            }
        }

class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    lyrics = Column(Text)
    chords = Column(Text, default='')
    likes = Column(Integer, default=0)
    made_by = Column(String(20), ForeignKey('user.username'), default='AntonisNikos')
    public = Column(Boolean, default=False)

    # Relationships
    composers = relationship("Composer", secondary="wrotemusic", back_populates="songs")
    lyricists = relationship("Lyricist", secondary="wrotelyrics", back_populates="songs")
    shared_with_teams = relationship("Team", secondary="teams_share_songs", back_populates="shared_songs")

class SongModel(BaseModel):
    id: int = Field(default=None, title="Song ID", description="Unique identifier for the song")
    title: str = Field(..., title="Song Title", description="Title of the song")
    lyrics: str = Field(..., title="Song Lyrics", description="Lyrics of the song")
    chords: str = Field(default='', title="Song Chords", description="Chords of the song")
    likes: int = Field(default=0, title="Likes", description="Number of likes for the song")
    made_by: str = Field(default='AntonisNikos', title="Made By", description="Username of the user who created the song")
    public: bool = Field(default=False, title="Public", description="Whether the song is public or not")
    composers: list[str] = Field(default=[], title="Composers", description="List of composers for the song")
    lyricists: list[str] = Field(default=[], title="Lyricists", description="List of lyricists for the song")
    shared_with_teams: list[str] = Field(default=[], title="Shared With Teams", description="List of teams that the song is shared with")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Song Title",
                "lyrics": "These are the lyrics of the song.",
                "chords": "C G Am F",
                "likes": 10,
                "made_by": "AntonisNikos",
                "public": True,
                "composers": ["Composer1", "Composer2"],
                "lyricists": ["Lyricist1", "Lyricist2"],
                "shared_with_teams": ["Team1", "Team2"]
            }
        }

class UpdateLyricsChordsModel(BaseModel):
    song_id: int = Field(..., title="Song ID", description="Unique identifier for the song")
    lyrics: str = Field(..., title="Song Lyrics", description="Lyrics of the song")
    chords: str = Field(..., title="Song Chords", description="Chords of the song")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "song_id": 1,
                "lyrics": "These are the updated lyrics of the song.",
                "chords": "C G Am F"
            }
        }

class UpdateChordsModel(BaseModel):
    song_id: int = Field(..., title="Song ID", description="Unique identifier for the song")
    chords: str = Field(..., title="Song Chords", description="Chords of the song")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "song_id": 1,
                "chords": "C G Am F"
            }
        }

class Composer(Base):
    __tablename__ = 'composer'

    name = Column(String(50), primary_key=True)

    # Relationships
    songs = relationship("Song", secondary="wrotemusic", back_populates="composers")

class Lyricist(Base):
    __tablename__ = 'lyricist'

    name = Column(String(50), primary_key=True)

    # Relationships
    songs = relationship("Song", secondary="wrotelyrics", back_populates="lyricists")

class WroteMusic(Base):
    __tablename__ = 'wrotemusic'

    composer = Column(String(50), ForeignKey('composer.name'), primary_key=True)
    song_id = Column(Integer, ForeignKey('song.id'), primary_key=True)

class WroteLyrics(Base):
    __tablename__ = 'wrotelyrics'

    lyricist = Column(String(50), ForeignKey('lyricist.name'), primary_key=True)
    song_id = Column(Integer, ForeignKey('song.id'), primary_key=True)

class Team(Base):
    __tablename__ = 'team'

    name = Column(String(50), primary_key=True)
    team_id = Column(String(50), unique=True, nullable=False)

    # Relationships
    members = relationship("MemberOfTeam", backref="team")
    shared_songs = relationship("Song", secondary="teams_share_songs", back_populates="shared_with_teams")

class MemberOfTeam(Base):
    __tablename__ = 'member_of_team'

    username = Column(String(20), ForeignKey('user.username'), primary_key=True)
    teamname = Column(String(50), ForeignKey('team.name'), primary_key=True, default='NTUA')
    points = Column(Integer)

class TeamsShareSongs(Base):
    __tablename__ = 'teams_share_songs'

    teamname = Column(String(50), ForeignKey('team.name'), primary_key=True)
    song_id = Column(Integer, ForeignKey('song.id'), primary_key=True)

# Create engine
DB_TYPE, DATABASE_URL = db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)