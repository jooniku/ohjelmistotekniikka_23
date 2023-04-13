import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.user import User
from repositories.user_repository import UserRepository
from services.log_entry_service import (log_entry_service,
                                        InvalidCredentialsError,
                                        UsernameAlreadyInUseError)


class TestLogEntryService(unittest.TestCase):

    def setUp(self):
        initialize_database()

    def test_after_login_service_has_correct_user(self):
        test_user = User('hi', '123')
        log_entry_service.create_new_user(
            test_user.username, test_user.password)

        log_entry_service.login('hi', '123')

        self.assertEqual(log_entry_service.user.username, test_user.username)

    def test_wrong_pw_on_login_raises_error(self):
        log_entry_service.create_new_user('test', '123')

        self.assertRaises(InvalidCredentialsError,
                          lambda: log_entry_service.login('test', '453'))

    def test_unavailiable_username_in_creating_new_user_raises_exception(self):
        log_entry_service.create_new_user('test', '123')

        self.assertRaises(UsernameAlreadyInUseError,
                          lambda: log_entry_service.create_new_user('test', '234'))

    def test_after_logout_service_has_no_user(self):
        test_user = User('hi', '123')
        log_entry_service.create_new_user(
            test_user.username, test_user.password)

        log_entry_service.login('hi', '123')

        log_entry_service.logout()

        self.assertEqual(log_entry_service.user, None)
