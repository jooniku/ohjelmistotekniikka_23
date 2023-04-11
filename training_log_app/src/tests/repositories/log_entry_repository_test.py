import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from repositories.log_entry_repository import LogEntryRepository
from entities.log_entry import LogEntry
from entities.user import User
import datetime


class TestLogEntryRepository(unittest.TestCase):
    def setUp(self):
        self.entry_repo = LogEntryRepository(get_database_connection())

        initialize_database()

        date = datetime.datetime.today()
        duration = 90
        session_style = 'wrestling'
        what_went_well = 'got a sweet firemans carry'
        what_did_not_go_well = 'got chocked'
        goal_for_next_session = 'get 3 singles'
        was_last_goal_achieved = True
        user_id = 1

        self.first_entry = LogEntry(user_id, date, duration, session_style, what_went_well,
                                    what_did_not_go_well, goal_for_next_session,
                                    was_last_goal_achieved)

        self.second_entry = LogEntry(user_id=2)

        self.user = User('userman', 'hellowalls')  # has user_id 1

    def test_create_entry_returns_entry(self):
        attempt = self.entry_repo._create_entry(self.first_entry)

        self.assertEqual(attempt, self.first_entry)

    def test_created_entry_has_correct_id_num(self):
        first = self.entry_repo._create_entry(self.first_entry)

        second = self.entry_repo._create_entry(self.second_entry)

        self.assertEqual(self.first_entry.log_id, 1)
        self.assertEqual(self.second_entry.log_id, 2)
