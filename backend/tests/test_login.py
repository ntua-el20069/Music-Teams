# import os
import os
import time
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
        self.valid_credentials = {"username": "admin0", "password": "admin0"}
        self.invalid_credentials = {"username": "admin0", "password": "wrong_password"}

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
        self.assertEqual(response_data["user_details"]["username"], "admin0")

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
        self.assertIn("Could not validate credentials", response.json()["detail"])

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
        self.valid_credentials = {"username": "admin0", "password": "admin0"}
        self.invalid_credentials = {"username": "admin0", "password": "wrong_password"}

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
        self.assertEqual(response_data["user_details"]["username"], "admin0")

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
        self.assertIn("Could not validate credentials", response.json()["detail"])

    def test_token_refresh(self):
        #################
        #  do the login
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,  # expect to redirect to home page after login
        )
        response_data = response.json()
        # after the redirect, the response should be a redirect to the home page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["user_details"]["username"], "admin0")
        access_token_1 = self.session.cookies.get("access_token")

        #######################
        # try to refresh the token
        refresh_response = self.session.get(
            f"{BASE_URL}/home/token-refresh", allow_redirects=True
        )
        if TEST_DEBUG:
            print(f"Token refresh response: {refresh_response.text}")
        self.assertEqual(refresh_response.status_code, 200)
        self.assertIn("access_token", self.session.cookies.get_dict())
        access_token_2 = self.session.cookies.get("access_token")
        self.assertNotEqual(access_token_1, access_token_2)

        ##########################
        # logout
        logout_response = self.session.get(
            f"{BASE_URL}/home/logout", allow_redirects=False
        )
        if TEST_DEBUG:
            print("Logout response:", logout_response.text)
        self.assertEqual(logout_response.status_code, 303)

    def test_check_token_expiration(self):
        """
        Test the check_token endpoint to ensure it redirects
        correctly based on token expiration.
        """
        # First, log in to get a valid token
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

        # Now, check the token expiration
        check_response = self.session.get(
            f"{BASE_URL}/home/check-token", allow_redirects=False
        )
        if TEST_DEBUG:
            print(f"Check token response: {check_response.text}")

        # Expect a redirect to /home if the token is still valid
        self.assertEqual(check_response.status_code, 303)

        # wait for the half of the token expiration time

        half_expiration_time = int(os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "16")) // 2
        time.sleep(
            half_expiration_time + 1
        )  # Add a second to ensure we cross the threshold

        # Check the token again
        check_response = self.session.get(
            f"{BASE_URL}/home/check-token", allow_redirects=False
        )
        if TEST_DEBUG:
            print(f"Check token response after waiting: {check_response.text}")

        # Expect a redirect to /home/token-refresh if the token is about to expire
        self.assertEqual(check_response.status_code, 307)

        # logout now
        logout_response = self.session.get(
            f"{BASE_URL}/home/logout", allow_redirects=False
        )
        if TEST_DEBUG:
            print("Logout response:", logout_response.text)

        self.assertEqual(logout_response.status_code, 303)
