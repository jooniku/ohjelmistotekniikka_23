class User:
    '''Class for a single user.
    User gets id after it's created from database.

    Attributes:
        id = int
        username: string
        password: string
    '''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None

    def add_id(self, user_id):
        '''Add id for User object.
        Get from database upon creation.

        Args:
            user_id: users id, created in the database
        '''

        self.user_id = user_id
