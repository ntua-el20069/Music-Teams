"""
FastAPI application for Music Teams All-Endpoints API.
Based on the concepts from backend/all.py but implemented with FastAPI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import public, myteams, specific_team

# Create FastAPI app instance
app = FastAPI(
    title="Music Teams All-Endpoints API",
    description="API for accessing composers, lyricists, and songs across different access scenarios",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(public.router, prefix="/public", tags=["public"])
app.include_router(myteams.router, prefix="/myteams", tags=["myteams"])
app.include_router(specific_team.router, prefix="/specific_team", tags=["specific_team"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Music Teams All-Endpoints API",
        "version": "1.0.0",
        "endpoints": {
            "public": [
                "GET /public/all-composers",
                "GET /public/all-lyricists", 
                "GET /public/all-songs"
            ],
            "myteams": [
                "GET /myteams/all-composers",
                "GET /myteams/all-lyricists",
                "GET /myteams/all-songs"
            ],
            "specific_team": [
                "GET /specific_team/all-composers?team_name=<name>",
                "GET /specific_team/all-lyricists?team_name=<name>",
                "GET /specific_team/all-songs?team_name=<name>"
            ]
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}