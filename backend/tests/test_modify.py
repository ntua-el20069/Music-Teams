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


class TestModifyUserDetails(unittest.TestCase):
    def setUp(self):
        print("Setting up the test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin0", "password": "admin0"}

        # Log in to get a session
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # logout
        logout_response = self.session.get(
            f"{BASE_URL}/home/logout",
            allow_redirects=False,
        )
        if TEST_DEBUG:
            print(f"Logout response: {logout_response.text}")

        # Expect a redirect to the frontend URL
        self.assertEqual(logout_response.status_code, 303)

        print("Tearing down the test environment...")

        self.session.close()

    def test_modify_user_details(self):

        # Modify user details
        modify_data = {"username": "new_admin", "password": "new_admin_password"}
        modify_response = self.session.post(
            f"{BASE_URL}/profile/update_user_details",
            json=modify_data,
            allow_redirects=False,
        )

        if TEST_DEBUG:
            print(f"Modify response: {modify_response.text}")

        # successfully redirect to logout page
        self.assertEqual(modify_response.status_code, 303)

        # change back to original credentials
        modify_data = {"username": "admin0", "password": "admin0"}
        modify_response = self.session.post(
            f"{BASE_URL}/profile/update_user_details",
            json=modify_data,
            allow_redirects=False,
        )
        if TEST_DEBUG:
            print(f"Modify response: {modify_response.text}")

        # successfully redirect to logout page
        self.assertEqual(modify_response.status_code, 303)

    def test_invalid_modify_user_details(self):

        # Attempt to modify user details with invalid data
        modify_data = {
            "username": "",  # Invalid username
            "password": "new_admin_password",
        }
        modify_response = self.session.post(
            f"{BASE_URL}/profile/update_user_details",
            json=modify_data,
            allow_redirects=False,
        )

        if TEST_DEBUG:
            print(f"Invalid modify response: {modify_response.text}")

        # Expect an error response
        self.assertEqual(modify_response.status_code, 400)
        self.assertIn("detail", modify_response.json())
        self.assertIn("Username cannot be empty", modify_response.json()["detail"])
