import bcrypt
from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    # class in charge of database operations for users

    def __init__(self, db_connection):
        self._db_connection = db_connection

    def user_availiable(self, username):
        '''
        Args: username

        Check if username is availiable.
        Is not availiable if it is found
        in the database'''

        cursor = self._db_connection.cursor()

        find = cursor.execute('''select username from Users where username=?''', [
                              username]).fetchone()

        if find is None:
            return True

        find = find[0]

        return find is username

    def get_user_id(self, username):
        '''Get a specified users id
        It is assumed the user exists'''
        cursor = self._db_connection.cursor()

        user_id = cursor.execute('''select id
        from users where username=?''', [username]).fetchone()[0]

        return user_id

    def create_user(self, user: User):
        '''
        Args: user


        Save user to database.
        Hash password with salt.

        App prompts login page after this
        '''

        cursor = self._db_connection.cursor()

        hashed_password = bcrypt.hashpw(
            user.password.encode('utf-8'), bcrypt.gensalt(12))

        cursor.execute('''insert into Users (username, password)
                        values (?,?)''', [user.username, hashed_password])

        self._db_connection.commit()

        return user

    def compare_passwords(self, username, password_attempt):
        '''Grab corresponding username and password form database
        and compare hashed passwords'''

        cursor = self._db_connection.cursor()

        user_password = cursor.execute('''select password from Users where
                        username=?''', [username]).fetchone()

        self._db_connection.commit()

        if user_password is None:
            return False

        user_password = user_password[0]

        return bcrypt.checkpw(password_attempt.encode('utf-8'), user_password)


user_repository = UserRepository(get_database_connection())
