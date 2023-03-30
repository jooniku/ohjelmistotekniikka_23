import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.user import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_george = User(username='george', password='ilovedinosaurs')
        self.user_sam = User(username='sam', password='ilovepotatoes')
        self.repo = UserRepository(get_database_connection())

    def test_user_creation_returns_user(self):
        usr = self.repo.create_user(self.user_george)
        self.assertEqual(usr, self.user_george)

    def test_after_user_creation_user_has_correct_id(self):
        create1 = self.repo.create_user(self.user_george)
        create2 = self.repo.create_user(self.user_sam)


        self.assertEqual(self.user_george.id, 1)
        self.assertEqual(self.user_sam.id, 2)