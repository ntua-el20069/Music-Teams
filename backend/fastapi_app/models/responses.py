"""
Pydantic models for API responses.
"""

from pydantic import BaseModel
from typing import List


class ComposersResponse(BaseModel):
    """Response model for all-composers endpoints."""
    composers: List[str]
    count: int

    class Config:
        json_schema_extra = {
            "example": {
                "composers": ["John Lennon", "Paul McCartney", "George Harrison"],
                "count": 3
            }
        }


class LyricistsResponse(BaseModel):
    """Response model for all-lyricists endpoints."""
    lyricists: List[str]
    count: int

    class Config:
        json_schema_extra = {
            "example": {
                "lyricists": ["Bob Dylan", "Leonard Cohen", "Joni Mitchell"],
                "count": 3
            }
        }


class SongsResponse(BaseModel):
    """Response model for all-songs endpoints."""
    songs: List[str]
    count: int

    class Config:
        json_schema_extra = {
            "example": {
                "songs": ["Yesterday", "Hey Jude", "Let It Be"],
                "count": 3
            }
        }


class ErrorResponse(BaseModel):
    """Response model for errors."""
    detail: str
    error_code: str = "GENERIC_ERROR"

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "An error occurred",
                "error_code": "GENERIC_ERROR"
            }
        }