from entities.log_entry import LogEntry
from entities.user import User
from database_connection import get_database_connection

class LogEntryRepository:
    # class to handle database stuff for log entries

    def __init__(self):
        '''Constructor function'''
        self.database = get_database_connection()

    def get_entry_with_user(self, user: User):
        '''Return users entries.
        
        Arguments: username - which users entries
        
        Returns: Specified users entries.'''
        pass

    def _create_entry(self, log_entry: LogEntry):
        '''Create entry to database.
        Log_entry itself has user_id with it.
        
        Arguments: log_entry - the entry to add
        
        Returns: boolean for successful creation'''
        cursor = self.database.cursor()

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
        
        log_id = cursor.execute('''select max(id) from Log_entries where user_id=?''', [log_entry.user_id]).fetchone()[0]

        self.database.commit()

        log_entry._add_id(log_id)