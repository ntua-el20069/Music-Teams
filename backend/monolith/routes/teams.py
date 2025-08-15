import os
from typing import Annotated, List

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import TeamCodeModel, TeamModel
from backend.monolith.routes.home import get_current_user
from backend.monolith.utils.team_ops import (
    all_teams,
    check_team_participation_threshold,
    insert_team,
    leave_team,
    participate_in_team,
)
from backend.monolith.utils.token import convert_to_jwt_token

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
FRONTEND_URL = os.getenv("FRONTEND_URL")

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


def get_teams_of_user(
    request: Request, current_user: dict = Depends(get_current_user)
) -> List[TeamModel]:
    """
    Middleware to get the teams of the current user.
    This will be used to fetch the teams data from the cookie.
    """
    token = request.cookies.get("team_data")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_428_PRECONDITION_REQUIRED,
            detail="Team token not found. \
                Please access again the my teams page.",
        )

    http_exc = HTTPException(
        status_code=status.HTTP_428_PRECONDITION_REQUIRED,
        detail="Team token does not contain teams data or invalid. \
            Please access again the my teams page.",
    )
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"require": ["teams"]},
        )

        teams = payload.get("teams")
        if teams is None:
            raise http_exc

        # Convert dicts to TeamModel instances
        teams = [TeamModel(**team) for team in teams]

        return teams

    except JWTError:
        raise http_exc


@router.get("/create-team", summary="Create a new team")
async def create_team(
    db: db_dependency, team_name: str, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Create a new team for the current user. \n
    Returns: \n
        JSONResponse with status 200 and success message \n
        with team details (team_name, team_code). \n
        removes the 'team_data' cookie \n
    Raises: \n
        HTTPException if team creation fails. \n
        status code 401 if the user is not authenticated. (see /home for more) \n
        status code 404 if the user is not found. or the new team to be enrolled is not found \n
        status code 409 if there exists a team with the same team_name \n
        status code 412 if user participates in max number of teams \n
        status code 500 for internal server errors. \n
    """
    # Implementation of team creation logic goes here.
    try:
        # Call the function that checks if the user participates
        # strictly less than MAX_TEAMS_TO_PARTICIPATE teams.
        can_create_team, msg = check_team_participation_threshold(
            db, current_user["user_id"]
        )

        if not can_create_team:
            if "error" in msg:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
                )
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED, detail=msg
            )

        # Call the function that creates a new team
        # and returns the team details.
        new_team, msg = insert_team(db, team_name)
        if not new_team:
            if "same name" in msg:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=msg)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        # set the user to participate in this team
        enrolled_in_team, msg = participate_in_team(
            db, current_user["user_id"], new_team.team_id
        )
        if not enrolled_in_team:
            if "Not found team with code" in msg:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        response = JSONResponse(
            status_code=200,
            content=TeamModel(
                team_name=new_team.team_name, team_id=new_team.team_id
            ).model_dump(),
        )

        # delete cookie so that the user needs to access the /teams/teams endpoint again
        # for the team data to be updated.
        response.delete_cookie(
            key="team_data",
            path="/",  # Make cookie available to all routes
        )

        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while creating the team.",
        )


@router.post("/enter-team", summary="Enter a new team with code")
async def enter_team(
    db: db_dependency,
    team_code_instance: TeamCodeModel,
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    """
    Enter a new team with the provided team code. \n
    Args: \n
        team_code (str): The unique code of the team to enter. \n
    Returns: \n
        JSONResponse with status 200 and success message \n
        if the user successfully enters the team. \n
        removes the 'team_data' cookie \n
    Raises: \n
        HTTPException if entering the team fails. \n
        status code 401 if the user is not authenticated. (see /home for more) \n
        status code 404 if the user is not found or the team with the provided code does
        not exist. \n
        status code 412 if the user participates in the maximum number of teams allowed. \n
        status code 500 for internal server errors. \n
    """
    try:
        team_code = team_code_instance.team_code

        # check participation threshold
        can_enter_team, msg = check_team_participation_threshold(
            db, current_user["user_id"]
        )

        if not can_enter_team:
            if "error" in msg:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
                )
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED, detail=msg
            )

        # enter the new team
        enrolled_in_team, msg = participate_in_team(
            db, current_user["user_id"], team_code
        )
        if not enrolled_in_team:
            if "Not found team with code" in msg:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        response = JSONResponse(status_code=200, content={"message": msg})

        # delete cookie so that the user needs to access the /teams/teams endpoint again
        # for the team data to be updated.
        response.delete_cookie(
            key="team_data",
            path="/",  # Make cookie available to all routes
        )

        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while entering the team.",
        )


@router.get("/leave-team", summary="Leave a team")
async def leave_team_route(
    db: db_dependency, team_name: str, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Leave the team specified. \n
    Args: \n
        team_name (str): The name of the team to leave. \n
    Returns: \n
        JSONResponse with status 200 and success message \n
        if the user successfully leaves the team. \n
        removes the 'team_data' cookie \n
    Raises: \n
        HTTPException if leaving the team fails. \n
        status code 401 if the user is not authenticated. (see /home for more) \n
        status code 404 if the user is not found or the user is not a member of the team. \n
        status code 500 for internal server errors. \n
    """
    try:
        # Logic to leave the team goes here.
        # This should remove the user from their current team.
        # If no team is found, raise an HTTPException with status 404.

        # function leave_team is called to remove the user from the team
        # and delete the team if it has no members left.
        success, msg = leave_team(db, current_user["user_id"], team_name)

        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)

        response = JSONResponse(status_code=200, content={"message": msg})

        # delete cookie so that the user needs to access the /teams/teams endpoint again
        # for the team data to be updated.
        response.delete_cookie(
            key="team_data",
            path="/",  # Make cookie available to all routes
        )

        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while leaving the team.",
        )


@router.get("/teams", summary="Get all teams")
async def get_teams(
    db: db_dependency, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Get all teams that the user is a member of. \n
    Returns: \n
        JSONResponse with status 200 and a list of teams \n
        that the user is a member of. \n
        sets the 'team_data' cookie with the details  \n
        of all teams in which the user is a member. \n
    Raises: \n
        HTTPException if fetching teams fails. \n
        status code 401 if the user is not authenticated. (see /home for more) \n
        status code 500 for internal server errors. \n
    """
    try:
        # use all_teams function to get all teams that the user is a member of
        success, msg, teams_instances = all_teams(db, current_user["user_id"])

        # Convert TeamModel instances to dicts
        teams = [team.model_dump() for team in teams_instances]

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        teams_data_token = convert_to_jwt_token(data={"teams": teams})

        response = JSONResponse(
            status_code=200, content={"message": msg, "teams": teams}
        )

        response.set_cookie(
            key="team_data",
            value=teams_data_token,
            httponly=True,  # TODO: how to set on production?
            secure=False,  # TODO: Set to True in production with HTTPS
            samesite="lax",  # Changed from "strict" to allow top-level navigation
            path="/",  # Make cookie available to all routes
            max_age=31536000,  # TODO: decide the expiration time - 1 year now
        )

        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while fetching teams.",
        )


@router.get("/team_details", summary="Get details of a specific team")
async def get_team_details(
    db: db_dependency,
    team_name: str,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Get details of a specific team by its name. \n
    Args: \n
        team_name (str): The name of the team to get details for. \n
    Returns: \n
        JSONResponse with status 200 and team details (team_name, team_code) if found. \n
    Raises: \n
        HTTPException if fetching team details fails. \n
        status code 401 if the user is not authenticated. (see /home for more) \n
        status code 404 if the team is not found \
            or the user is not registered in this team. \n
        status code 500 for internal server errors. \n

    """
    try:
        found_teams = [team for team in teams if team.team_name == team_name]
        if not found_teams:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Team '{team_name}' \
                    does not exist or you are not registered in this team.",  # noqa: E713
            )
        found_team = found_teams[0]

        response = JSONResponse(status_code=200, content=found_team.model_dump())

        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while fetching team details.",
        )
