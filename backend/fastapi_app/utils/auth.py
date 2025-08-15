"""
Authentication utilities for FastAPI application.
"""

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from typing import Optional

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    """
    Get current authenticated user.
    Simple authentication for demo purposes.
    TODO: Implement proper authentication with JWT or session-based auth.
    """
    # Simple hardcoded authentication for demo
    # In production, this should validate against a proper user database
    correct_username = secrets.compare_digest(credentials.username, "demo_user")
    correct_password = secrets.compare_digest(credentials.password, "demo_password")
    
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return credentials.username


def team_if_enrolled(team_name: str, current_user: str = Depends(get_current_user)) -> str:
    """
    Check if user is enrolled in the specified team.
    TODO: Implement proper team enrollment check when team tables are available.
    
    Args:
        team_name: Name of the team to check
        current_user: Current authenticated user
        
    Returns:
        team_name if user is enrolled
        
    Raises:
        HTTPException: If user is not enrolled in the team
    """
    # Placeholder implementation
    # TODO: Replace with actual database query:
    # SELECT 1 FROM team_members WHERE user_id = %s AND team_name = %s
    
    # For demo, allow access to any team for authenticated users
    allowed_teams = ["team1", "team2", "demo_team"]
    
    if team_name not in allowed_teams:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User {current_user} is not enrolled in team '{team_name}'"
        )
    
    return team_name


def validate_team_name(team_name: Optional[str]) -> str:
    """
    Validate that team_name parameter is provided.
    
    Args:
        team_name: Team name from query parameter
        
    Returns:
        team_name if valid
        
    Raises:
        HTTPException: If team_name is missing
    """
    if not team_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="team_name parameter is required"
        )
    
    return team_name