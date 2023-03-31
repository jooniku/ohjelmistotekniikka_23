import unittest
from initialize_database import initialize_database
from repositories.log_entry_repository import LogEntryRepository
from entities.log_entry import LogEntry
from entities.user import User
import datetime

class TestLogEntryRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()

        date = datetime.datetime.today()
        duration = 90
        session_style = 'wrestling'
        what_went_well = 'got a sweet firemans carry'
        what_did_not_go_well = 'got chocked'
        goal_for_next_session = 'get 3 singles'
        was_last_goal_achieved = True
        user_id = 1

        self.entry = LogEntry(user_id, date, duration, session_style, what_went_well, 
                        what_did_not_go_well, goal_for_next_session,
                        was_last_goal_achieved)
        
        self.entry_repo = LogEntryRepository()
        
        self.user = User('userman', 'hellowalls')


    
    def test_create_legal_entry_returns_entry(self):
        attempt = self.entry_repo._create_entry(self.entry)

        self.assertEqual(attempt, self.entry)



    def test_created_legal_entry_has_correct_id_num(self):
        attempt = self.entry_repo._create_entry(self.entry)

        self.assertEqual(self.entry.log_id, 1)