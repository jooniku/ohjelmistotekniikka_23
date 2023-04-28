from entities.log_entry import LogEntry
from entities.user import User
from database_connection import get_database_connection


class LogEntryRepository:
    '''Class to handle the connection between
    LogEntryService and the database. Handles
    the LogEntry objects.
    
    Main functions:
        create_entry: saves new log entry to database
        get_users_log_entry_by_id: get users entry with entry's id
    '''

    def __init__(self, db_connection):
        '''Initialization function

        Args:
            db_connection: database to connect to
        '''

        self.database = db_connection

        # different session styles are defined here and the database init file
        self.session_styles = ['wrestling', 'grappling',
                         'striking', 'sparring', 'other']

    def get_session_styles(self):
        '''Return different session styles defined here.
        '''
        return self.session_styles
    

    def get_users_log_entry_by_id(self, user: User, log_id: int):
        '''Get a specific users specific log entry
        from database. 

        Args:
            user (User): which user
            log_id (int): logs user specific id
        '''

        cursor = self.database.cursor()

        entry = cursor.execute('''select * from
                                Log_entries
                                where log_id=? and
                                user_id=?''',
                               [log_id, user.user_id]).fetchall()

        self.database.commit()

        return entry

    def get_all_entries_with_user(self, user: User):
        '''Return users entries.

        Args: username - which users entries

        Returns: Specified users entries.
        '''

        cursor = self.database.cursor()

        entry_list = cursor.execute('''select * from Log_entries where
                                 user_id=? order by log_id desc''', [user.user_id]).fetchone()

        self.database.commit()

        return entry_list

    def get_total_time_spent_by_user(self, user: User):
        '''Returns total time (sum of durations)
        user has spent training.

        Args: user - which user

        Return: sum of durations
        '''

        cursor = self.database.cursor()

        time = cursor.execute('''select ifnull(sum(duration),0)
                                from Log_entries where user_id=?''',
                              [user.user_id]).fetchone()

        return time[0]

    def get_amount_of_goals_achieved_by_user(self, user: User):
        '''Returns a tuple containing (a, b)
        where a represents how many times user
        has achieved a set goal and b represents
        amount of all entries by user.

        Arg: user - which user

        Return: specified tuple
        '''

        cursor = self.database.cursor()

        goals_achieved = cursor.execute('''select ifnull(count(*),0)
                                        from Log_entries where user_id=?
                                        and was_last_goal_achieved=1''',
                                        [user.user_id]).fetchone()[0]

        amount_of_entries = cursor.execute('''select ifnull(count(*),0)
                                        from Log_entries where user_id=?''',
                                           [user.user_id]).fetchone()[0]

        self.database.commit()

        return goals_achieved, amount_of_entries

    def get_users_last_entry_id(self, user: User):
        '''Return users last entry's id.

        Args: user - which user
        '''

        cursor = self.database.cursor()

        entry_id = cursor.execute('''select log_id from Log_entries
                                where user_id=? 
                                order by id desc limit 1''',
                                  [user.user_id]).fetchone()

        self.database.commit()

        return None if entry_id is None else entry_id[0]

    def create_entry(self, user: User, log_entry: LogEntry):
        '''Create a new log entry to database.

        Args:
            user (User): which users entry
            log_entry (LogEntry): the entry content
        '''

        cursor = self.database.cursor()

        last_log_id = self.get_users_last_entry_id(user=user)
        if last_log_id is None:
            last_log_id = 0
        last_log_id += 1

        cursor.execute('''insert into Log_entries (
                    log_id,
                    user_id,
                    date,
                    duration,
                    session_style,
                    what_went_well,
                    what_did_not_go_well,
                    goal_for_next_session,
                    was_last_goal_achieved) 
                    values (?,?,?,?,?,?,?,?,?)''',
                       [last_log_id, log_entry.user_id, log_entry.date, log_entry.duration,
                        log_entry.session_style, log_entry.what_went_well,
                        log_entry.what_did_not_go_well, log_entry.goal_for_next_session,
                        log_entry.was_last_goal_achieved])

        self.database.commit()

    def get_users_session_styles_ranked(self, user: User):
        '''Get a specific users session styles
        with count of each of them. Uses helper dictionary
        so even if no entrys for session it's displayed.

        Args: user - which user
        
        Returns:
            sorted list where (amount of sessions, style name)
        '''
        
        style_count = {}
        for style in self.session_styles: style_count[style] = 0

        cursor = self.database.cursor()
        data = cursor.execute('''select session_style, count(session_style)
                                from Log_entries where
                                user_id=? group by session_style
                                ''', [user.user_id]).fetchall()
        self.database.commit()

        for session_style, count in data:
            if session_style == 'select':
                continue
            style_count[session_style] += count

        return sorted([(style_count[style], style) for style in style_count.keys()], reverse=True)

    def get_all_training_dates_by_user(self, user: User):
        '''Get all training session dates
        by specific user from the database as a list.

        Args: user - which users data
        '''
        
        cursor = self.database.cursor()

        dates = cursor.execute('''select date from Log_entries
                        where user_id=?''', [user.user_id]).fetchall()

        self.database.commit()

        return [date[0] for date in dates]


log_entry_repository = LogEntryRepository(get_database_connection())
