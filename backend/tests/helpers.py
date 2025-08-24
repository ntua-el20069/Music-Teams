from typing import Tuple

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True
NUM_USERS = 2  # Number of admin users to create for testing


def login_user(session: requests.Session, credentials: dict) -> Tuple[bool, int, str]:

    response = session.post(
        f"{BASE_URL}/simple_login/login",
        json=credentials,
        allow_redirects=True,  # expect to redirect to home page after login
    )
    if TEST_DEBUG:
        print(f"Login response: {response.text}")
    # after the redirect, the response should be a redirect to the home page
    status_code_ok = response.status_code == 200
    # user_ok = ( response_data["user_details"]["username"] == credentials["username"] )
    token_obtained = "access_token" in session.cookies.get_dict()
    if status_code_ok and token_obtained:
        return (True, response.status_code, response.text)
    else:
        return (False, response.status_code, response.text)


def logout_user(session: requests.Session) -> Tuple[bool, int, str]:
    logout_response = session.get(f"{BASE_URL}/home/logout", allow_redirects=False)
    if TEST_DEBUG:
        print("Logout response:", logout_response.text)
    status_code_ok = logout_response.status_code == 303
    token_removed = "access_token" not in session.cookies.get_dict()
    if status_code_ok and token_removed:
        return (True, logout_response.status_code, logout_response.text)
    else:
        return (False, logout_response.status_code, logout_response.text)


def create_team(session: requests.Session, team_name: str) -> Tuple[bool, int, str]:
    team_response = session.get(f"{BASE_URL}/teams/create-team?team_name={team_name}")
    if TEST_DEBUG:
        print(f"Create team response: {team_response.text}")
    status_code_ok = team_response.status_code == 200
    if status_code_ok:
        return (True, team_response.status_code, team_response.text)
    else:
        return (False, team_response.status_code, team_response.text)


def leave_team(session: requests.Session, team_name: str) -> Tuple[bool, int, str]:
    leave_response = session.get(f"{BASE_URL}/teams/leave-team?team_name={team_name}")
    if TEST_DEBUG:
        print(f"Leave team response: {leave_response.text}")
    status_code_ok = leave_response.status_code == 200
    if status_code_ok:
        return (True, leave_response.status_code, leave_response.text)
    else:
        return (False, leave_response.status_code, leave_response.text)


def get_teams(session: requests.Session) -> Tuple[bool, int, str]:
    teams_response = session.get(f"{BASE_URL}/teams/teams", timeout=10)
    if TEST_DEBUG:
        print(f"Get teams response: {teams_response.text}")
    status_code_ok = teams_response.status_code == 200
    team_date_cookie_present = "team_data" in session.cookies.get_dict()
    if status_code_ok and team_date_cookie_present:
        return (True, teams_response.status_code, teams_response.text)
    else:
        return (False, teams_response.status_code, teams_response.text)
