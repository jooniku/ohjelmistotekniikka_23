from database_connection import get_database_connection


def drop_tables(db_connection):
    cursor = db_connection.cursor()

    cursor.execute('''drop table if exists Users;''')
    cursor.execute('''drop table if exists Log_entries;''')
    db_connection.commit()


def create_tables(db_connection):
    cursor = db_connection.cursor()

    cursor.execute('''create table Users 
                    (id integer primary key, 
                    username text, 
                    password text);''')

    cursor.execute('''create table Log_entries
                    (id integer primary key,
                    user_id reference Users,
                    date text,
                    duration integer,
                    session_style text,
                    what_went_well text,
                    what_did_not_go_well text,
                    goal_for_next_session text,
                    was_last_goal_achieved bool);''')

    db_connection.commit()


def initialize_database():
    db_connection = get_database_connection()

    drop_tables(db_connection)
    create_tables(db_connection)


if __name__ == "__main__":
    initialize_database()
