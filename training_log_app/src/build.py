from initialize_database import initialize_database


def build():
    '''This creates a new SQL database.
    This function is called with a poetry command.
    '''

    initialize_database()


if __name__ == "__main__":
    build()
