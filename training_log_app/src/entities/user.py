class User:
    '''Class for a single user. 
    
    Attributes:
        username: string
        password: string
    '''

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password