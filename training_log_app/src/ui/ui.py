from tkinter import ttk
from ui.new_log_entry_view import NewLogEntryView
from ui.login_view import LoginView
from ui.create_new_user_view import CreateNewUserView
from ui.main_user_page_view import MainUserPageView
from ui.statistics_view import StatisticsPageView
from ui.browse_log_entries_view import BrowseLogEntriesView
from services.log_entry_service import log_entry_service


class UI:
    '''Class responsible for user interface'''

    def __init__(self, root):
        '''
        Arguments:
            root:
                Tkinter element to create the ui in'''

        self._root = root
        self._current_view = None

        self._theme = log_entry_service.load_theme()

        self.configure_window()

    def configure_window(self):
        self._root.resizable(width=False, height=False)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _change_theme(self):
        '''Changes applications theme.
        '''
        if self._theme == 'DayMode':
            self._theme = 'NightMode'
        else:
            self._theme = 'DayMode'

        log_entry_service.save_theme(current_theme=self._theme)
        self._show_main_user_page()

    def start(self):
        '''Starts ui.
        '''

        self._show_login_view()

    def _show_new_log_entry_view(self):
        '''Displays new log entry creation page.
        '''

        self._hide_current_view()

        self._current_view = NewLogEntryView(self._root,
                                             self._show_main_user_page,
                                             theme=self._theme)

        self._current_view.pack()

    def _show_login_view(self):
        '''Displays login page.
        '''

        self._hide_current_view()

        self._current_view = LoginView(self._root,
                                       self._show_main_user_page,
                                       self._show_create_new_user_view,
                                       theme=self._theme)

        self._current_view.pack()

    def _show_main_user_page(self):
        '''Displays main page.
        '''

        self._hide_current_view()
        self._current_view = MainUserPageView(self._root,
                                              self._show_login_view,
                                              self._show_new_log_entry_view,
                                              self._show_statistics_page_view,
                                              self._show_browse_log_entries_view,
                                              self._change_theme,
                                              theme=self._theme)
        self._current_view.pack()

    def _show_create_new_user_view(self):
        '''Displays new user creation page.
        '''

        self._hide_current_view()

        self._current_view = CreateNewUserView(self._root,
                                               self._show_login_view,
                                               theme=self._theme)

        self._current_view.pack()

    def _show_statistics_page_view(self):
        '''Displays statistics page.
        '''

        self._hide_current_view()

        self._current_view = StatisticsPageView(self._root,
                                                self._show_main_user_page,
                                                theme=self._theme)

        self._current_view.pack()

    def _show_browse_log_entries_view(self):
        '''Displays browsing log entries page.
        '''

        self._hide_current_view()

        self._current_view = BrowseLogEntriesView(self._root,
                                                  self._show_main_user_page,
                                                  theme=self._theme)

        self._current_view.pack()
