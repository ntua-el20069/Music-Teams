# import os
import unittest

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

# BASE_URL = (
#     "http://fastapi-app:8000/login"
#     if str(os.getenv("MODE")) == "CONTAINER"
#     else "http://localhost:8000/login"
# )
BASE_URL = "http://127.0.0.1:8000"  # Adjust for your local setup
TEST_DEBUG = True


class TestLoginLogout(unittest.TestCase):
    def setUp(self):
        print("Setting up the test environment...")
        self.session = requests.Session()
        self.multiple_sessions = [requests.Session() for _ in range(4)]
        self.valid_credentials = {"username": "admin", "password": "admin"}
        self.invalid_credentials = {"username": "admin", "password": "wrong_password"}

    def tearDown(self):
        print("Tearing down the test environment...")
        self.session.close()
        for session in self.multiple_sessions:
            session.close()

    def test_valid_login_logout(self):
        ######################################
        # do the login
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,  # expect to redirect to home page after login
        )
        response_data = response.json()
        if TEST_DEBUG:
            print(f"Login response: {response.text}")
        # after the redirect, the response should be a redirect to the home page
        self.assertEqual(response.status_code, 200)

        self.assertIn("message", response_data)
        self.assertEqual(response_data["user_details"]["username"], "admin")

        ######################################
        # Logout after successful login
        # (keep the session alive in order to keep the access_token cookie)
        if TEST_DEBUG:
            print("Cookies: ", self.session.cookies.get_dict())
        self.assertIn("access_token", self.session.cookies.get_dict())

        logout_response = self.session.get(
            f"{BASE_URL}/home/logout", allow_redirects=False
        )
        if TEST_DEBUG:
            print("Logout response:", logout_response.text)
        self.assertEqual(logout_response.status_code, 303)

    def test_invalid_login(self):
        response = self.session.post(
            f"{BASE_URL}/simple_login/login", json=self.invalid_credentials
        )
        if TEST_DEBUG:
            print(f"Invalid login response: {response.text}")
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Invalid username or password")

    def test_invalid_logout(self):
        response = self.session.get(
            f"{BASE_URL}/home/logout", cookies={"access_token": "invalid_token"}
        )
        if TEST_DEBUG:
            print(f"Invalid logout response: {response.text}")
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Could not validate credentials")

    def test_sessions_restriction(self):
        # Attempt to create multiple sessions
        for i in range(4):
            response = self.multiple_sessions[i].post(
                f"{BASE_URL}/simple_login/login",
                json=self.valid_credentials,
                allow_redirects=True,  # expect to redirect to home page after login
            )
            if TEST_DEBUG:
                print(f"Session {i} response: {response.text}")
            if i < 3:
                self.assertEqual(response.status_code, 200)
            else:
                self.assertEqual(response.status_code, 400)
                self.assertIn(
                    "You have reached the maximum number of active sessions (3)",
                    response.json()["detail"],
                )
        # Logout from the 3 sessions
        for i in range(3):
            logout_response = self.multiple_sessions[i].get(
                f"{BASE_URL}/home/logout", allow_redirects=False
            )
            self.assertEqual(logout_response.status_code, 303)


class TestHome(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin", "password": "admin"}
        self.invalid_credentials = {"username": "admin", "password": "wrong_password"}

    def tearDown(self):
        self.session.close()

    def test_login_and_home_and_logout(self):
        #################
        #  do the login
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,  # expect to redirect to home page after login
        )
        response_data = response.json()
        if TEST_DEBUG:
            print(f"Login response: {response.text}")
        # after the redirect, the response should be a redirect to the home page
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response_data)
        self.assertEqual(response_data["user_details"]["username"], "admin")

        #######################
        # check the home route
        home_response = self.session.get(f"{BASE_URL}/home/")
        if TEST_DEBUG:
            print(f"Home response: {home_response.text}")
        self.assertEqual(home_response.status_code, 200)

        ###################################
        # logout after successful login
        # (keep the session alive in order to keep the access_token cookie)
        if TEST_DEBUG:
            print("Cookies: ", self.session.cookies.get_dict())
        self.assertIn("access_token", self.session.cookies.get_dict())

        logout_response = self.session.get(
            f"{BASE_URL}/home/logout", allow_redirects=False
        )
        if TEST_DEBUG:
            print("Logout response:", logout_response.text)
        self.assertEqual(logout_response.status_code, 303)

    def test_check_access_invalid_token(self):
        # Attempt to access home route with an invalid token
        response = self.session.get(
            f"{BASE_URL}/home/", cookies={"access_token": "invalid_token"}
        )
        if TEST_DEBUG:
            print(f"Invalid token response: {response.text}")
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Could not validate credentials")
