from tkinter import ttk, constants
from services.log_entry_service import log_entry_service


class MainUserPageView:
    '''Class for main users page interface'''

    def __init__(self, root, login_view, new_entry_view):
        self._root = root
        self._frame = None
        # self._all_user_entries_view
        self._login_view = login_view
        self._new_entry_view = new_entry_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout(self):
        log_entry_service.logout()
        self._login_view()

    def _handle_new_entry(self):
        self._new_entry_view()

    def _initialize(self):
        # initialize window

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text='Main Page')

        user_id = log_entry_service.user.id
        username = log_entry_service.user.username
        user_data = ttk.Label(
            master=self._frame, text=f'Logged in as {username}, with id of {user_id}')

        new_log_entry_button = ttk.Button(master=self._frame,
                                          text='New Log Entry',
                                          command=self._handle_new_entry)

        logout_button = ttk.Button(master=self._frame,
                                   text='Log out',
                                   command=self._handle_logout)

        # build ui

        heading_label.grid(row=0, column=0)

        user_data.grid(row=1, column=0)

        new_log_entry_button.grid(row=0, column=2)

        logout_button.grid(row=2, column=1)
