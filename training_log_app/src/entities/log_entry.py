
class LogEntry:
    '''Class for a single log entry.

    All attributes are None by default.
    It is not necessary to give any information upon creation except user id.
    After creation more info can be added.

    Attributes:
        date: type string
        duration: type integer in minutes
        session_style: type string   e.g. boxing, wrestling, perhaps multiple choice?
        what_went_well: type string
        what_did_not_go_well: type string
        goal_for_next_session: type string
        was_last_goal_achieved: type int, 1 for True, 0 for False
        user_id: type int
        log_entry_id: type int created in database
    '''

    # I believe this is the simplest way to construct an entry so pylint is disabled
    #pylint: disable=too-many-instance-attributes
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.date = None
        self.duration = None
        self.session_style = None
        self.what_went_well = None
        self.what_did_not_go_well = None
        self.goal_for_next_session = None
        self.was_last_goal_achieved = None
        self.log_id = None

    def add_id(self, id):
        self.log_id = id
