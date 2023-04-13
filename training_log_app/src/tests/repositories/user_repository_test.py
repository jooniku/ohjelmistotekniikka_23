import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.user import User
from repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_george = User(username='george', password='ilovedinosaurs')
        self.user_sam = User(username='sam', password='ilovepotatoes')
        self.repo = UserRepository(get_database_connection())
        initialize_database()

    def test_user_creation_returns_user(self):
        usr = self.repo.create_user(self.user_george)
        self.assertEqual(usr, self.user_george)

    def test_getting_user_id_returns_correct_id(self):
        self.repo.create_user(self.user_george)

        id = self.repo.get_user_id(self.user_george.username)

        self.assertEqual(id, 1)

    def test_user_availiable_finds_username_already_taken(self):
        self.repo.create_user(self.user_george)

        is_availiable = self.repo.user_availiable('george')

        self.assertEqual(is_availiable, False)

    def test_password_comparison_returns_true_for_correct_pw(self):
        self.repo.create_user(self.user_george)

        comp = self.repo.compare_passwords('george', 'ilovedinosaurs')

        self.assertEqual(comp, True)

    def test_password_comparison_returns_false_for_incorrect_pw(self):
        self.repo.create_user(self.user_george)

        comp = self.repo.compare_passwords('george', 'incorrectpw')

        self.assertEqual(comp, False)
