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
        entry = LogEntry()

        entry.user_id = self.user.id

        entry.date = content['date']
        entry.duration = content['duration']
        entry.session_style = content['session_style']
        entry.what_went_well = content['what_went_well']
        entry.what_did_not_go_well = content['what_did_not_go_well']
        entry.goal_for_next_session = content['goal_for_next_session']
        entry.was_last_goal_achieved = content['was_last_goal_achieved']

        # check if input is valid !!!!!!!!!!!!!!!!!!!!!!!
        # if not raise InvalidInputError

        self.log_entry_repository.create_entry(entry)

    def logout(self):
        self.user = None

    def get_total_time_spent_training(self):
        # returns total training time by user
        return self.log_entry_repository.get_total_time_spent_by_user(self.user)
    
    def get_precentage_of_goals_achieved(self):
        # returns the precentage of set goals user has achieved in training
        data = self.log_entry_repository.get_amount_of_goals_achieved_by_user(self.user)

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
        if self.user_repository.user_availiable(username):
            self.user_repository.create_user(
                User(username=username, password=password))
        else:
            raise UsernameAlreadyInUseError

    def get_last_entry_goal(self):
        # returns previously set goal for session
        return self.log_entry_repository.get_last_entry_with_user(self.user)[7]


log_entry_service = LogEntryService()
