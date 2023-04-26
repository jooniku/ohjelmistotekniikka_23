class User:
    '''Class for a single user. 

    Attributes:
        id = int
        username: string
        password: string

        user gets id after it's created from database
    '''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None

    def add_id(self, user_id):
        '''Add id for User object.
        Get from database upon creation.'''

        self.user_id = user_id
