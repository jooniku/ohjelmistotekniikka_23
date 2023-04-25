from datetime import datetime
from entities.log_entry import LogEntry
from entities.user import User

from repositories.log_entry_repository import (
    log_entry_repository as default_log_entry_repository
)

# both call get database connection, might not be good

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameAlreadyInUseError(Exception):
    pass


class InvalidInputError(Exception):
    pass


class LogEntryService:
    '''Class in charge of application logic,
    connects user and log entries'''

    def __init__(self,
                 log_entry_repository=default_log_entry_repository,
                 user_repository=default_user_repository):

        self.user = None
        self.log_entry_repository = log_entry_repository
        self.user_repository = user_repository

    def create_log_entry(self, content: dict):
        '''Creates a new log entry using
        log_entry_repository. Input validation
        is performed here.

        Args:
            content (dict): content of log entry
        '''
        entry = LogEntry()

        entry.user_id = self.user.id

        entry.date = content['date']
        entry.duration = content['duration']
        entry.session_style = content['session_style']
        entry.what_went_well = content['what_went_well']
        entry.what_did_not_go_well = content['what_did_not_go_well']
        entry.goal_for_next_session = content['goal_for_next_session']
        entry.was_last_goal_achieved = content['was_last_goal_achieved']

        # date validation is done automatically with the selector
        try:
            entry.duration = int(entry.duration)
        except ValueError as exc:
            raise InvalidInputError from exc

        self.log_entry_repository.create_entry(entry)

    def logout(self):
        '''Logs user out'''

        self.user = None

    def get_total_time_spent_training(self):
        '''Accesses log_entry_repository to 
        get total time spent training by user.'''

        return self.log_entry_repository.get_total_time_spent_by_user(self.user)

    def get_total_amount_of_training_sessions(self):
        '''Accesses log_entry_repository to
        get total amount of training sessions
        by user.'''

        return self.log_entry_repository.get_amount_of_goals_achieved_by_user(self.user)[1]

    def get_precentage_of_goals_achieved(self):
        '''Calculates the precentage of set goals that the user
        has achieved (marked so in the log entry page)
        via log_entry_repository.'''

        data = self.log_entry_repository.get_amount_of_goals_achieved_by_user(
            self.user)

        achieved = data[0]

        # minus one since the first entry has not achieved goal
        # so the calculation would be incorrect
        total_goals = data[1] - 1

        return (achieved / total_goals) * 100 if total_goals > 0 else 0

    def get_last_log_entry(self):
        # returns users latest entry
        return self.log_entry_repository.get_last_entry_with_user(self.user)

    def _get_user_id(self):
        return self.user_repository.get_user_id(self.user.username)

    def login(self, username, password):
        if not self.user_repository.compare_passwords(username, password):
            raise InvalidCredentialsError

        self.user = User(username=username, password=password)

        self.user.add_id(self._get_user_id())

    def create_new_user(self, username, password):
        if username == '' or password == '' or ' ' in password or ' ' in username:
            raise InvalidInputError

        if self.user_repository.user_availiable(username):
            self.user_repository.create_user(
                User(username=username, password=password))
        else:
            raise UsernameAlreadyInUseError
        

    def get_last_entry_goal(self):
        # returns previously set goal for session
        return self.log_entry_repository.get_last_entry_with_user(self.user)[7]

    def get_current_training_instances(self):
        '''Using log_entry_repository gets 
        all training dates and counts sessions
        for this year, month and week.

        Returns: tuple - (year, month, week)
        of how many sessions'''

        dates = self.log_entry_repository.get_all_training_dates_by_user(
            self.user)

        current_week = datetime.today().isocalendar()[1]
        current_year = datetime.today().year
        current_month = datetime.today().month

        sessions_this_year = 0
        sessions_this_month = 0
        session_this_week = 0

        for date in dates:
            date = datetime.strptime(date, '%d/%m/%Y').date()
            if date.year == current_year:
                sessions_this_year += 1
            if date.month == current_month:
                sessions_this_month += 1
            if date.isocalendar()[1] == current_week:
                session_this_week += 1

        return sessions_this_year, sessions_this_month, session_this_week

    def get_weekly_user_training_instances_this_year(self):
        '''Accessing the log_entry_repository
        gets all of the dates for current user
        and calculates for each week instances of sessions.
        E.g. week 2 has 3 sessions, week 4 has 2 sessions.

        Returns: list instances where index is week'''

        current_year = datetime.today().year

        session_dates = self.log_entry_repository.get_all_training_dates_by_user(
            self.user)

        training_instances = [0 for _ in range(53)]

        for date in session_dates:
            date = datetime.strptime(date, '%d/%m/%Y').date()
            if date.year == current_year:
                training_instances[date.isocalendar()[1]] += 1

        return training_instances[1:]

    def get_users_session_styles_ranked(self):
        '''Gets users session styles
        ranked by most common style to least
        common.'''
        return self.log_entry_repository.get_users_session_styles_ranked(self.user)


log_entry_service = LogEntryService()
