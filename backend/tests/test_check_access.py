# using pytest and FastAPI's TestClient to test the check_access endpoint
import unittest

from dotenv import load_dotenv
from fastapi.testclient import TestClient

from backend.monolith.app import app

env_path = ".env"
load_dotenv(dotenv_path=env_path)

TestClient = TestClient(app)


class TestCheckAccess(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_access_valid_token(self):
        # TODO: implement testcases
        assert 201 == 200
