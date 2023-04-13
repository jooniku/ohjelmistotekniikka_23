from entities.log_entry import LogEntry
from entities.user import User
from database_connection import get_database_connection


class LogEntryRepository:
    # class to handle database stuff for log entries

    def __init__(self, db_connection):
        '''Constructor function'''
        self.database = db_connection

    #pylint: disable=unused-argument
    # under construction so pylint is not happy
    def get_entry_with_user(self, user: User):
        '''Return users entries.

        Arguments: username - which users entries

        Returns: Specified users entries.'''
        # under construction so pylint check unnecessary
        pass #pylint: disable=unnecessary-pass

    def get_last_entry_with_user(self, user: User):
        # find entry by user with largest id
        return 'under construction'

    def create_entry(self, log_entry: LogEntry):
        '''Create entry to database.
        Log_entry itself has user_id with it.

        Arguments: log_entry - the entry to add
        '''
        cursor = self.database.cursor()

        cursor.execute('''insert into Log_entries (
                    user_id,
                    date,
                    duration,
                    session_style,
                    what_went_well,
                    what_did_not_go_well,
                    goal_for_next_session,
                    was_last_goal_achieved) 
                    values (?,?,?,?,?,?,?,?)''',
                       [log_entry.user_id, log_entry.date, log_entry.duration,
                        log_entry.session_style, log_entry.what_went_well,
                        log_entry.what_did_not_go_well, log_entry.goal_for_next_session,
                        log_entry.was_last_goal_achieved])

        log_id = cursor.execute('''select max(id) from Log_entries where user_id=?''', [
                                log_entry.user_id]).fetchone()[0]

        self.database.commit()

        log_entry.add_id(log_id)

        return log_entry


log_entry_repository = LogEntryRepository(get_database_connection())
