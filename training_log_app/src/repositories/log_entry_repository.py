from entities.log_entry import LogEntry
from database_connection import get_database_connection

class LogEntryRepository:
    # class to handle database stuff for log entries

    def __init__(self, filepath):
        '''Constructor function'''
        self.database = get_database_connection()

    def get_entry_with_username(self, username: str):
        '''Return users entries.
        
        Arguments: username - which users entries
        
        Returns: Specified users entries.'''
        pass

    def create_entry_with_username(self, username: str, log_entry: LogEntry):
        '''Create entry for user.
        
        Arguments: username - which users entry
                   log_entry - the entry to add
        
        Returns: boolean for successful creation'''
        cursor = self.database.cursor()

        try:
            cursor.execute('''insert into Log_entries (
                        date,
                        duration,
                        session_style,
                        what_went_well,
                        what_did_not_go_well,
                        goal_for_next_session,
                        was_last_goal_achieved,
                        user_id reference Users) 
                        values (?,?,?,?,?,?,?,?)''',
                        [log_entry.date, log_entry.duration,
                        log_entry.session_style, log_entry.what_went_well,
                        log_entry.what_did_not_go_well, log_entry.goal_for_next_session,
                        log_entry.was_last_goal_achieved, log_entry.user_id])    
            self.database.commit()
        except: 
            return False
        return True


# for testing

import datetime
date = datetime.datetime.today()
duration = 90
session_style = 'wrestling'
what_went_well = 'got a sweet double leg'
what_did_not_go_well = 'got chocked'
goal_for_next_session = 'get 3 singles'
was_last_goal_achieved = True
user_id = 1

entry = LogEntry(date, duration, session_style, what_went_well, 
                 what_did_not_go_well, goal_for_next_session,
                 was_last_goal_achieved, user_id)

con = LogEntryRepository()

con.create_entry_with_username(entry)