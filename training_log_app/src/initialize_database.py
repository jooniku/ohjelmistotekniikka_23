from database_connection import get_database_connection


def drop_tables(db_connection):
    '''Drops all tables for current database.
    Shouldn't be called in normal use, but useful
    for testing.

    Args:
        db_connection: connection to the database
    '''

    cursor = db_connection.cursor()

    cursor.execute('''drop table if exists Users;''')
    cursor.execute('''drop table if exists Log_entries;''')
    db_connection.commit()


def create_tables(db_connection):
    '''Create necessary tables in the database.

    Args:
        db_connection: connection to the database
    '''

    cursor = db_connection.cursor()

    cursor.execute('''create table Users
                    (id integer primary key,
                    username text,
                    password text);''')

    cursor.execute('''create table Log_entries
                    (id integer primary key,
                    log_id integer,
                    user_id reference Users,
                    date text,
                    duration integer,
                    session_style text,
                    what_went_well text,
                    what_did_not_go_well text,
                    goal_for_next_session text,
                    was_last_goal_achieved integer);''')

    db_connection.commit()


def initialize_database():
    '''Gets a connection to a database configured in the
    .env file and initializes it for use.
    '''

    db_connection = get_database_connection()

    drop_tables(db_connection)
    create_tables(db_connection)


if __name__ == "__main__":
    initialize_database()
