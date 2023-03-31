from entities.user import User

class LogEntry:
    '''Class for a single log entry.
    
    All attributes are None by default (except was_last_goal_achieved, which is boolean).
    It is not necessary to give any information, except date and user.

    Attributes:
        date: type datetime.date
        duration: type integer in minutes
        session_style: type string   e.g. boxing, wrestling, perhaps multiple choice?
        what_went_well: type string
        what_did_not_go_well: type string
        goal_for_next_session: type string
        was_last_goal_achieved: type bool
        user_id: type int
        log_entry_id: type int created in database
    '''

    def __init__(self, user_id, date=None, duration=None, session_style=None, what_went_well=None, what_did_not_go_well=None, goal_for_next_session=None, was_last_goal_achieved=False):
        self.user_id = user_id
        self.date = date
        self.duration = duration
        self.session_style = session_style
        self.what_went_well = what_went_well
        self.what_did_not_go_well = what_did_not_go_well
        self.goal_for_next_session = goal_for_next_session
        self.was_last_goal_achieved = was_last_goal_achieved
        self.log_id = None

    def _add_id(self, id):
        self.log_id = id
    