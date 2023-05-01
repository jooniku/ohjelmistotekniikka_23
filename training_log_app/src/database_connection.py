import sqlite3
from config import DATABASE_FILEPATH


db_connection = sqlite3.connect(DATABASE_FILEPATH)
db_connection.row_factory = sqlite3.Row


def get_database_connection():
    return db_connection

