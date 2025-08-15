import os
import uuid
from typing import Optional, Tuple

from dotenv import load_dotenv
from sqlalchemy import exc as sqlalchemy_exc
from sqlalchemy.orm import Session

from backend.monolith.models.models import MemberOfTeam, Team, TeamModel

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)


def check_team_participation_threshold(db: Session, user_id: str) -> Tuple[bool, str]:
    try:

        number_of_teams_participating = (
            db.query(MemberOfTeam).filter(MemberOfTeam.user_id == user_id).count()
        )
        if number_of_teams_participating >= int(
            os.getenv("MAX_TEAMS_TO_PARTICIPATE", "10")
        ):
            return (False, "User participates in max number of teams allowed")

        return (True, "User can enter a new team")

    except Exception as exc:
        print(exc)
        return (
            False,
            f"Unexpected error during check_team_participation_threshold: {exc}",
        )


def insert_team(db: Session, team_name: str) -> Tuple[Optional[TeamModel], str]:
    try:
        # check if exists team with team_name
        found_team = db.query(Team).filter(Team.name == team_name).first()
        if found_team:
            return (None, "There exists another team with the same name")

        # make a random team code, check that is unique else retry
        max_retries = 10
        team_code = ""
        for i in range(max_retries):
            team_code = str(uuid.uuid4())[:50]
            team_found = db.query(Team).filter(Team.team_id == team_code).first()
            if i == max_retries - 1 and team_found:
                return (
                    None,
                    f"Could not generate unique team code after {max_retries} tries",
                )
            if not team_found:
                break

        new_team = Team(name=team_name, team_id=team_code)
        db.add(new_team)
        db.commit()
        db.refresh(new_team)

        return (
            TeamModel(team_name=new_team.name, team_id=new_team.team_id),
            "Team created successfully",
        )

    except Exception as exc:
        print(exc)
        return (None, f"Unexpected error during team insertion: {exc}")


def participate_in_team(db: Session, user_id: str, team_code: str) -> Tuple[bool, str]:
    try:
        found_team = db.query(Team).filter(Team.team_id == team_code).first()

        if not found_team:
            return (False, f"Not found team with code {team_code}")

        member = MemberOfTeam(user_id=user_id, teamname=found_team.name)

        db.add(member)
        db.commit()

        return (True, f"User successfully enrolled in team {found_team.name}")

    except sqlalchemy_exc.IntegrityError as exc:
        db.rollback()
        print(exc)
        return (False, f"User is already enrolled in team {found_team.name}")

    except Exception as exc:
        print(exc)
        return (False, f"Unexpected error during enrolling user in team {exc}")


def leave_team(db: Session, user_id: str, team_name: str) -> Tuple[bool, str]:
    try:
        member = (
            db.query(MemberOfTeam)
            .filter(MemberOfTeam.user_id == user_id, MemberOfTeam.teamname == team_name)
            .first()
        )

        if not member:
            return (
                False,
                f"User is not a member of team \
                    {team_name} or {team_name} does not exist",
            )

        number_of_team_members = (
            db.query(MemberOfTeam).filter(MemberOfTeam.teamname == team_name).count()
        )

        db.delete(member)
        msg = f"User {user_id} successfully left team {team_name}"

        if number_of_team_members <= 1:
            # if the team has only one member, delete the team
            msg += " and the team was deleted"
            db.query(Team).filter(Team.name == team_name).delete()

        db.commit()  # single commit for both delete operations

        return (True, msg)

    except Exception as exc:
        db.rollback()
        print(exc)
        return (False, f"Unexpected error during leaving team: {exc}")


def all_teams(db: Session, user_id: str) -> Tuple[bool, str, list[TeamModel]]:
    try:
        teams = (
            db.query(Team)
            .join(MemberOfTeam, Team.name == MemberOfTeam.teamname)
            .filter(MemberOfTeam.user_id == user_id)
            .all()
        )

        if not teams:
            return (True, "No teams found for the user.", [])

        return (
            True,
            "Teams found for the user.",
            [TeamModel(team_name=team.name, team_id=team.team_id) for team in teams],
        )

    except sqlalchemy_exc.SQLAlchemyError as exc:
        print(exc)
        return (False, f"Database error during fetching teams: {exc}", [])
    except Exception as exc:
        print(exc)
        return (False, f"Unexpected error during fetching teams: {exc}", [])
