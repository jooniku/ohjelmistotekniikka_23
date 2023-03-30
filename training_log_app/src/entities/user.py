class User:
    '''Class for a single user. 
    
    Attributes:
        id = int
        username: string
        password: string

        user gets id after it's created from database
    '''

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.id = None

    def add_id(self, id):
        '''
        Add id for object
        Get from database upon creation
        '''
        self.id = id