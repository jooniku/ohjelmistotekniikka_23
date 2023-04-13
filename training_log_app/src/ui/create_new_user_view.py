from tkinter import ttk, constants
from services.log_entry_service import log_entry_service, UsernameAlreadyInUseError


class CreateNewUserView:
    '''Class for the ui of creating a new user'''

    def __init__(self, root, login_view) -> None:
        self._root = root
        self._show_login_view = login_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_new_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            log_entry_service.create_new_user(username, password)
            print('user created successfully')
            self._show_login_view()
        except UsernameAlreadyInUseError:
            print('Username already taken')

    def _initialize(self):
        # initialize window

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text='Create new user')

        username_label = ttk.Label(master=self._frame, text='Username:')
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text='Password:')
        self._password_entry = ttk.Entry(master=self._frame)

        create_button = ttk.Button(master=self._frame,
                                   text='Create user',
                                   command=self._handle_create_new_user)

        # make go back button

        # build the ui

        heading_label.grid(row=0, column=0)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        create_button.grid(row=3, column=1)
