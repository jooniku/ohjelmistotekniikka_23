from entities.log_entry import LogEntry
from entities.user import User

from repositories.log_entry_repository import (
    log_entry_repository as default_log_entry_repository
)

# both call get database connection, might not be good

from repositories.user_repository import (
    user_repository as default_user_repository
)

class LogEntryService:
    '''Class in charge of application logic,
    connects user and log entries'''
    
    def __init__(self,
                log_entry_repository=default_log_entry_repository,
                user_repository=default_user_repository):
        
        self.user = None
        self.log_entry_repository = log_entry_repository
        self.user_repository = user_repository


    def create_log_entry(self, content:dict):
        entry = LogEntry()

        
        #entry.user_id = self.user.id

        entry.date = content['date']
        entry.duration = content['duration']
        entry.session_style = content['session_style']
        entry.what_went_well = content['what_went_well']
        entry.what_did_not_go_well = content['what_did_not_go_well']
        entry.goal_for_next_session = content['goal_for_next_session']
        entry.was_last_goal_achieved = content['was_last_goal_achieved']
        

        self.log_entry_repository._create_entry(entry)



    def login(self):
        pass

log_entry_service = LogEntryService()