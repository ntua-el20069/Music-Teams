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
BASE_URL = "http://localhost:8000/login"  # Adjust for your local setup


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login_valid_token(self):
        response = requests.post(
            f"{BASE_URL}/login", params={"username": "admin", "password": "admin"}
        )
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response_data)
        self.assertIsInstance(response_data["token"], str)
        self.assertGreater(len(response_data["token"]), 0)
        # Logout after successful login
        token = response_data.get("token")
        self.assertIsNotNone(token)
        logout_response = requests.post(f"{BASE_URL}/logout", params={"token": token})
        self.assertEqual(logout_response.status_code, 200)

    def test_login_invalid(self):
        response = requests.post(
            f"{BASE_URL}/login",
            params={"username": "invalid_user", "password": "invalid_pass"},
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Invalid username or password")


class TestCheckAccess(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_access_valid_token(self):
        response = requests.post(
            f"{BASE_URL}/login", params={"username": "admin", "password": "admin"}
        )
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response_data)
        self.assertIsInstance(response_data["token"], str)
        token = response_data.get("token")
        self.assertIsNotNone(token)
        access_response = requests.post(
            f"{BASE_URL}/check_access", params={"token": token}
        )
        self.assertEqual(access_response.status_code, 200)
        access_data = access_response.json()
        self.assertIn("role", access_data)
        self.assertIn("username", access_data)
        self.assertEqual(access_data["role"], "admin")
        self.assertEqual(access_data["username"], "admin")
        # logout
        logout_response = requests.post(f"{BASE_URL}/logout", params={"token": token})
        self.assertEqual(logout_response.status_code, 200)

    def test_check_access_invalid_token(self):
        response = requests.post(
            f"{BASE_URL}/check_access", params={"token": "invalid_token"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Invalid or expired session token")


class TestLogout(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_logout_valid_token(self):
        response = requests.post(
            f"{BASE_URL}/login", params={"username": "admin", "password": "admin"}
        )
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response_data)
        self.assertIsInstance(response_data["token"], str)
        token = response_data.get("token")
        self.assertIsNotNone(token)
        logout_response = requests.post(f"{BASE_URL}/logout", params={"token": token})
        self.assertEqual(logout_response.status_code, 200)
        self.assertIn("message", logout_response.json())
        self.assertEqual(
            logout_response.json()["message"], "Session removed successfully"
        )

    def test_logout_invalid_token(self):
        response = requests.post(
            f"{BASE_URL}/logout", params={"token": "invalid_token"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())

    def test_sessions_restriction(self):
        # Attempt to create multiple sessions
        # use an array of tokens to track active sessions
        tokens = []
        for i in range(4):
            response = requests.post(
                f"{BASE_URL}/login",
                params={"username": "admin", "password": "admin"},
            )
            response_data = response.json()
            if i < 3:
                self.assertEqual(response.status_code, 200)
                tokens.append(response_data.get("token"))
            else:
                self.assertEqual(response.status_code, 401)
                self.assertIn(
                    "You have reached the maximum number of active sessions (3)",
                    response.json()["detail"],
                )
        # Logout from the 3 sessions
        for token in tokens[:3]:
            logout_response = requests.post(
                f"{BASE_URL}/logout", params={"token": token}
            )
            self.assertEqual(logout_response.status_code, 200)
            self.assertIn("message", logout_response.json())
            self.assertEqual(
                logout_response.json()["message"], "Session removed successfully"
            )
