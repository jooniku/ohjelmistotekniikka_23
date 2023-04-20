from entities.log_entry import LogEntry
from entities.user import User
from database_connection import get_database_connection


class LogEntryRepository:
    # class to handle database stuff for log entries

    def __init__(self, db_connection):
        '''Constructor function'''
        self.database = db_connection

    def get_all_entries_with_user(self, user: User):
        '''Return users entries.

        Arguments: username - which users entries

        Returns: Specified users entries.'''

        cursor = self.database.cursor()

        entry_list = cursor.execute('''select * from Log_entries where user_id=? order by id desc''', [user.id]).fetchone()

        self.database.commit()

        return entry_list  # untested
    
    def get_total_time_spent_by_user(self, user: User):
        '''Returns total time (sum of durations)
        user has spent training.
        
        Arg: user - which user
        
        Return: sum of durations'''

        cursor = self.database.cursor()

        time = cursor.execute('''select ifnull(sum(duration),0) from Log_entries where user_id=?''', [user.id]).fetchone()

        return time[0]


    def get_amount_of_goals_achieved_by_user(self, user: User):
        '''Returns a tuple containing (a, b)
        where a represents how many times user
        has achieved a set goal and b represents
        amount of all entries by user.
        
        Arg: user - which user
        
        Return: specified tuple'''

        cursor = self.database.cursor()

        goals_achieved = cursor.execute('''select ifnull(count(*),0) from Log_entries where user_id=? and was_last_goal_achieved=1''', [user.id]).fetchone()[0]

        amount_of_entries = cursor.execute('''select ifnull(count(*),0) from Log_entries where user_id=?''', [user.id]).fetchone()[0]

        self.database.commit()

        return goals_achieved, amount_of_entries # untested

    def get_last_entry_with_user(self, user: User):
        '''Return users last entry.
        Args: user - which user
        
        Returns: Users last entry. Or if no
        last entry, then text saying so.'''

        cursor = self.database.cursor()

        entry = cursor.execute('''select * from Log_entries where user_id=? order by id desc limit 1''', [user.id]).fetchall()

        self.database.commit()

        return 'No previous entries' if entry is None else list(entry[0])

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
