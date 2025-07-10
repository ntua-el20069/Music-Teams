import unittest

from dotenv import load_dotenv

env_path = ".env"
load_dotenv(dotenv_path=env_path)


class TestCheckAccess(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_access_valid_token(self):
        # TODO: implement testcases
        assert 201 == 200
