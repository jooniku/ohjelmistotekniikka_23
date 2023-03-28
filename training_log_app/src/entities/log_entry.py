class LogEntry:
    '''Class for a single log entry.
    
    All attributes are None by default (except was_last_goal_achieved, which is boolean).
    It is not necessary to give any information, except date, user and log_entry_id.

    Attributes:
        date: type datetime.date
        duration: type integer in minutes
        what_was_trained: type string
        what_went_well: type string
        what_did_not_go_well: type string
        goal_for_next_session: type string
        was_last_goal_achieved: type bool
        user: type User
        log_entry_id: type string
    '''

    def __init__(self, date=None, duration=None, what_was_trained=None, what_went_well=None, what_did_not_go_well=None, goal_for_next_session=None, was_last_goal_achieved=False, user=None, log_entry_id=None):
        self.date = date
        self.duration = duration
        self.what_was_trained = what_was_trained
        self.what_went_well = what_went_well
        self.what_did_not_go_well = what_did_not_go_well
        self.goal_for_next_session = goal_for_next_session
        self.was_last_goal_achieved = was_last_goal_achieved
        self.user = user
        self.id = log_entry_id

        
    