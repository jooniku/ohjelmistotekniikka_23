import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from repositories.log_entry_repository import LogEntryRepository
from entities.log_entry import LogEntry
from entities.user import User


class TestLogEntryRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.repo = LogEntryRepository(get_database_connection())

        self.first_entry = LogEntry()
        self.first_entry.date = '12/03/2023'
        self.first_entry.duration = 90
        self.first_entry.session_style = 'wrestling'
        self.first_entry.what_went_well = 'got a nice firemans carry'
        self.first_entry.what_did_not_go_well = 'got chocked'
        self.first_entry.goal_for_next_session = 'get 3 singles'
        self.first_entry.was_last_goal_achieved = 1
        self.first_entry.user_id = 1

        self.second_entry = LogEntry()
        self.second_entry.date = '01/12/2022'
        self.second_entry.duration = 45
        self.second_entry.session_style = 'striking'
        self.second_entry.what_went_well = 'found new combo'
        self.second_entry.what_did_not_go_well = 'hands drop easily'
        self.second_entry.goal_for_next_session = 'find combo in sparring'
        self.second_entry.was_last_goal_achieved = 0
        self.second_entry.user_id = 1

        self.user = User('userman', 'hellowalls')  # has user_id 1
        self.user.add_id(1)

    def test_created_entry_is_saved_correctly(self):
        self.repo.create_entry(self.user, self.first_entry)

        from_database = self.repo.get_users_log_entry_by_id(
            user=self.user, log_id=1)

        self.assertEqual(from_database[1], 1)
        self.assertEqual(from_database[2], self.first_entry.user_id)
        self.assertEqual(from_database[3], self.first_entry.date)
        self.assertEqual(from_database[4], self.first_entry.duration)
        self.assertEqual(from_database[5], self.first_entry.session_style)
        self.assertEqual(from_database[6], self.first_entry.what_went_well)
        self.assertEqual(from_database[7],
                         self.first_entry.what_did_not_go_well)
        self.assertEqual(from_database[8],
                         self.first_entry.goal_for_next_session)
        self.assertEqual(from_database[9],
                         self.first_entry.was_last_goal_achieved)

    def test_get_users_last_entry_id_is_one_if_one_entry(self):
        self.repo.create_entry(self.user, self.first_entry)

        entry_id = self.repo.get_users_last_entry_id(self.user)

        self.assertEqual(entry_id, 1)

    def test_get_users_last_entry_id_is_none_if_no_entries(self):
        entry_id = self.repo.get_users_last_entry_id(self.user)

        self.assertEqual(entry_id, None)

    def test_get_users_last_entry_id_adds_correctly(self):
        for i in range(10):
            self.repo.create_entry(self.user, self.first_entry)

        last_entry_id = self.repo.get_users_last_entry_id(self.user)

        self.assertEqual(last_entry_id, 10)

    def test_get_session_styles_returns_correct_list(self):
        # NOTE: this will fail if the list is changed even if
        # the actual underlying method works
        style_list = ['wrestling', 'grappling',
                      'striking', 'sparring', 'other']

        self.assertEqual(self.repo.get_session_styles(), style_list)

    def test_get_total_time_spent_by_user_adds_time_correctly(self):
        for i in range(10):
            self.repo.create_entry(self.user, self.first_entry)

        duration = self.repo.get_total_time_spent_by_user(self.user)

        self.assertEqual(duration, 10*90)

    def test_get_amount_of_goals_achieved_by_user_works_correctly(self):
        self.repo.create_entry(self.user, self.first_entry)
        self.repo.create_entry(self.user, self.second_entry)

        from_db = self.repo.get_amount_of_goals_achieved_by_user(self.user)

        goals_achieved = from_db[0]
        amount_of_entries = from_db[1]

        self.assertEqual(goals_achieved, 1)
        self.assertEqual(amount_of_entries, 2)

    def test_get_users_session_styles_ranked_works_with_no_entries(self):
        ranked = self.repo.get_users_session_styles_ranked(self.user)

        styles = self.repo.get_session_styles()

        self.assertEqual(len(ranked), len(styles))

    def test_get_users_session_styles_ranked_finds_number_one(self):
        self.repo.create_entry(self.user, self.first_entry)

        most_common_style = self.repo.get_users_session_styles_ranked(self.user)[
            0][1]

        self.assertEqual(most_common_style, self.first_entry.session_style)

    def test_get_users_session_styles_ranked_finds_number_two(self):
        for i in range(2):
            self.repo.create_entry(self.user, self.first_entry)
        self.repo.create_entry(self.user, self.second_entry)

        second_most_common = self.repo.get_users_session_styles_ranked(self.user)[
            1][1]

        self.assertEqual(second_most_common, self.second_entry.session_style)

    def test_if_session_style_is_select_it_is_not_counted(self):
        pass

    # plus testaa get_all_training_dates_by_user
