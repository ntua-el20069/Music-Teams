from typing import List

from pydantic import BaseModel


class HomeResponse(BaseModel):
    songs: List[str]
    ids: List[int]
    selected: str
