import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from repositories.log_entry_repository import LogEntryRepository
from entities.log_entry import LogEntry
from entities.user import User


class TestLogEntryRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()

        self.entry_repo = LogEntryRepository(get_database_connection())

        self.first_entry = LogEntry()
        self.first_entry.date = '12/03/2023'
        self.first_entry.duration = 90
        self.first_entry.session_style = 'wrestling'
        self.first_entry.what_went_well = 'got a sweet firemans carry'
        self.first_entry.what_did_not_go_well = 'got chocked'
        self.first_entry.goal_for_next_session = 'get 3 singles'
        self.first_entry.was_last_goal_achieved = 1

        self.user = User('userman', 'hellowalls')  # has user_id 1
        self.user.add_id(1)

    def test_created_entry_is_saved_correctly(self):
        self.entry_repo.create_entry(self.user, self.first_entry)

        from_database = self.entry_repo.get_users_log_entry_by_id(
            self.user, log_id=1)
        print(from_database)
        self.assertEqual(self.first_entry.date, from_database[1])
