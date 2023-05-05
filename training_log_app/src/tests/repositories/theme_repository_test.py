import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from repositories.theme_repository import ThemeRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.repo = ThemeRepository(get_database_connection())

        self.themes = ['DayMode', 'NightMode']

    def test_default_theme_is_DayMode(self):
        theme = self.repo.load_application_theme()

        self.assertEqual(theme, 'DayMode')

    def test_saving_works_correctly(self):
        theme = 'NightMode'

        self.repo.save_application_theme(theme=theme)

        theme_from_db = self.repo.load_application_theme()

        self.assertEqual(theme_from_db, theme)
