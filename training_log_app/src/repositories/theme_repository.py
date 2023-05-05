from database_connection import get_database_connection


class ThemeRepository:
    '''Class to handle saving
    and retrieving themes from database.
    Themes style the user interface.
    '''

    def __init__(self, db_connection):
        self._db_connection = db_connection

    def load_application_theme(self):
        '''Gets apps theme from database.

        Returns:
            string: theme
        '''

        cursor = self._db_connection.cursor()

        theme = cursor.execute('''select theme from Themes
                                where id=1''').fetchone()

        self._db_connection.commit()

        return theme[0]

    def save_application_theme(self, theme: str):
        '''Save current theme in the database to be
        loaded the next time. First deletes previously
        saved theme.

        Args:
            theme: theme to be saved
        '''

        cursor = self._db_connection.cursor()

        cursor.execute('''delete from Themes where id=1''')

        cursor.execute('''insert into Themes (theme)
                        values (?)''', [theme])

        self._db_connection.commit()


theme_repository = ThemeRepository(get_database_connection())
