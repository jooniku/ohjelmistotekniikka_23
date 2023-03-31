from entities.user import User
from database_connection import get_database_connection
import bcrypt


class UserRepository:
    # class in charge of database operations for users

    def __init__(self, db_connection):
        self._db_connection = db_connection

    def create_user(self, user: User):
        '''
        Args: user

        Save user to database.
        Hash password with salt.
        Get user id from database and give to user object.

        return: user
        '''

        cursor = self._db_connection.cursor()

        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt(12))

        cursor.execute('''insert into Users (username, password)
                        values (?,?)''', [user.username, hashed_password])

        user_id = cursor.execute('''select max(id) from Users''').fetchone()[0]

        self._db_connection.commit()

        user.add_id(user_id)

        return user
        