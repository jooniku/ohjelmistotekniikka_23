from ui.new_log_entry_view import NewLogEntryView
from ui.login_view import LoginView
from ui.create_new_user_view import CreateNewUserView
from ui.main_user_page_view import MainUserPageView


class UI:
    '''Class responsible for user interface'''

    def __init__(self, root):
        '''
        Arguments:
            root:
                Tkinter element to create the ui in'''

        self._root = root
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def start(self):
        '''Starts ui'''
        self._show_login_view()

    def _show_new_log_entry_view(self):
        self._hide_current_view()

        self._current_view = NewLogEntryView(self._root,
                                             self._show_main_user_page)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root,
                                       self._show_main_user_page,
                                       self._show_create_new_user_view)

        self._current_view.pack()

    def _show_main_user_page(self):
        self._hide_current_view()

        self._current_view = MainUserPageView(self._root,
                                              self._show_login_view,
                                              self._show_new_log_entry_view)
        # all user entries
        # etc.
        self._current_view.pack()

    def _show_create_new_user_view(self):
        self._hide_current_view()

        self._current_view = CreateNewUserView(self._root,
                                               self._show_login_view)

        self._current_view.pack()