import unittest
from datetime import datetime
from initialize_database import initialize_database
from database_connection import get_database_connection
from entities.user import User
from entities.log_entry import LogEntry
from repositories.user_repository import UserRepository
from repositories.log_entry_repository import LogEntryRepository
from services.log_entry_service import (log_entry_service,
                                        InvalidCredentialsError,
                                        UsernameAlreadyInUseError,
                                        InvalidInputError)


class TestLogEntryService(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.log_entry_repo = LogEntryRepository(get_database_connection())

        user = User('bilbo', 'baggins')
        log_entry_service.create_new_user(user.username, user.password)
        log_entry_service.login(user.username, user.password)

        self.entry = {}
        self.entry['date'] = '12/03/2023'
        self.entry['duration'] = 60
        self.entry['session_style'] = 'wrestling'
        self.entry['what_went_well'] = 'got a nice firemans carry'
        self.entry['what_did_not_go_well'] = 'got chocked'
        self.entry['goal_for_next_session'] = 'get 3 singles'
        self.entry['was_last_goal_achieved'] = 1

    def test_after_login_service_has_correct_user(self):
        log_entry_service.logout()

        test_user = User('hi', '123')
        log_entry_service.create_new_user(
            test_user.username, test_user.password)

        log_entry_service.login('hi', '123')

        self.assertEqual(log_entry_service.user.username, test_user.username)

    def test_wrong_pw_on_login_raises_error(self):
        self.assertRaises(InvalidCredentialsError,
                          lambda: log_entry_service.login('bilbo', 'notbaggins'))

    def test_space_in_name_upon_user_creation_raises_error(self):
        self.assertRaises(
            InvalidInputError, lambda: log_entry_service.create_new_user('h e', 'skf'))

    def test_space_in_password_upon_user_creation_raises_error(self):
        self.assertRaises(
            InvalidInputError, lambda: log_entry_service.create_new_user('hde', 'sk f'))

    def test_unavailiable_username_in_creating_new_user_raises_exception(self):
        self.assertRaises(UsernameAlreadyInUseError,
                          lambda: log_entry_service.create_new_user('bilbo', '234'))

    def test_after_logout_service_has_no_user(self):
        log_entry_service.logout()

        self.assertEqual(log_entry_service.user, None)

    def test_creating_log_entry_is_saved_and_fetched_correctly(self):
        log_entry_service.create_log_entry(self.entry)

        entry_from_db = log_entry_service.get_last_log_entry()

        self.assertEqual(entry_from_db[3], self.entry['date'])
        self.assertEqual(entry_from_db[4], self.entry['duration'])
        self.assertEqual(entry_from_db[5], self.entry['session_style'])
        self.assertEqual(entry_from_db[6], self.entry['what_went_well'])
        self.assertEqual(entry_from_db[7], self.entry['what_did_not_go_well'])
        self.assertEqual(entry_from_db[8], self.entry['goal_for_next_session'])
        self.assertEqual(entry_from_db[9],
                         self.entry['was_last_goal_achieved'])

    def test_creating_log_entry_with_illegal_duration_input_raises_error(self):
        self.entry['duration'] = 'this raises an error'
        self.assertRaises(
            InvalidInputError, lambda: log_entry_service.create_log_entry(self.entry))

    def test_get_latest_log_id_with_no_logs_returns_none(self):
        data = log_entry_service.get_latest_log_id()

        self.assertEqual(data, None)

    def test_get_latest_log_id_with_log_works_correctly(self):
        log_entry_service.create_log_entry(self.entry)

        log_id = log_entry_service.get_latest_log_id()

        self.assertEqual(log_id, 1)

    def test_get_total_time_spent_by_user_returns_correct_value(self):
        self.entry = {}
        self.entry['date'] = '12/03/2023'
        self.entry['duration'] = '60'
        self.entry['session_style'] = 'wrestling'
        self.entry['what_went_well'] = 'got a nice firemans carry'
        self.entry['what_did_not_go_well'] = 'got chocked'
        self.entry['goal_for_next_session'] = 'get 3 singles'
        self.entry['was_last_goal_achieved'] = 1

        log_entry_service.create_log_entry(self.entry)

        data = log_entry_service.get_total_time_spent_training()

        self.assertEqual(data, 60)

    def test_get_total_amount_of_training_sessions_returns_correct_amount(self):
        for i in range(3):
            log_entry_service.create_log_entry(self.entry)

        data = log_entry_service.get_total_amount_of_training_sessions()

        self.assertEqual(data, 3)

    def test_get_total_time_spent_training_returns_correct_amount(self):
        for i in range(3):
            log_entry_service.create_log_entry(self.entry)

        data = log_entry_service.get_total_time_spent_training()

        self.assertEqual(data, self.entry['duration']*3)

    def test_get_current_training_instances_works_correctly(self):
        current_date = datetime.now()
        date_string = current_date.strftime("%d/%m/%Y")

        self.entry['date'] = date_string

        for i in range(3):
            log_entry_service.create_log_entry(self.entry)

        data = log_entry_service.get_current_training_instances()

        self.assertEqual(data, (3, 3, 3))

    def test_get_weekly_training_instances_this_year_works_correctly(self):
        current_year = str(datetime.now().year)

        self.entry['date'] = '05/01/' + current_year
        print(self.entry['date'])
        for i in range(3):
            log_entry_service.create_log_entry(self.entry)

        data = log_entry_service.get_weekly_user_training_instances_this_year()

        self.assertEqual(data[1], 3)
