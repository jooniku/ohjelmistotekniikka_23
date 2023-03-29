from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    # class for database operations for users

    def __init__(self, db_connection):
        self.db_connection = db_connection