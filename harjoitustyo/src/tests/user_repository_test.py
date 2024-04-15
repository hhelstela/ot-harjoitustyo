import unittest
import datetime
from src.repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository("tests.db")
        self.user_repository.clear_all_users()
        self.user_repository.add_table_to_db()

    def test_add_user(self):
        self.user_repository.add_user("testuser", "testpass")
        self.assertEqual(self.user_repository.get_all_users()
                         [0][1], "testuser")

    def test_get_all_users(self):
        self.user_repository.add_user("testuser", "testpass")
        self.user_repository.add_user("testuser2", "testpass2")
        self.assertEqual(self.user_repository.get_all_users()
                         [0][1], "testuser")
        self.assertEqual(self.user_repository.get_all_users()
                         [1][1], "testuser2")

    def test_login_with_valid_account(self):
        self.user_repository.add_user("testuser", "testpass")
        self.assertEqual(self.user_repository.login_to_service(
            "testuser", "testpass"), True)

    def test_login_with_invalid_account(self):
        self.assertEqual(self.user_repository.login_to_service(
            "testuser", "testpass"), False)

    def test_login_with_invalid_password(self):
        self.user_repository.add_user("testuser", "testpass")
        self.assertEqual(self.user_repository.login_to_service(
            "testuser", "wrongpass"), False)

    def test_add_user_with_username_taken(self):
        self.user_repository.add_user("testuser", "testpass")
        self.assertEqual(self.user_repository.add_user(
            "testuser", "testpass"), False)
