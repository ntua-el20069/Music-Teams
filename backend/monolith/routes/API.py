from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional, Annotated
from backend.monolith.database.database import get_db
from backend.monolith.models.response_models import HomeResponse
from backend.monolith.models.models import Song

base_path = "monolith/"
router = APIRouter()

@router.get("/", response_description="API Home")
async def api_home():
    """
    Home route for the API.
    Returns a simple HTML response with a link to the API documentation.
    """
    html_content = None
    with open(base_path + "templates/API.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
