from tkinter import ttk, constants
from services.log_entry_service import log_entry_service, InvalidCredentialsError


class LoginView:
    '''Class for login ui'''

    def __init__(self, root, show_main_page, show_create_new_user):
        self._root = root
        self._show_main_page = show_main_page
        self._show_create_new_user = show_create_new_user

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            log_entry_service.login(username, password)
            self._show_main_page()

        except InvalidCredentialsError:
            print('Wrong password or username does not exist')

    def _handle_create_new_user_view(self):
        self._show_create_new_user()

    def _initialize(self):
        # initialize window

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text='Login or create new user')

        username_label = ttk.Label(master=self._frame, text='Username:')
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text='Password:')
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(master=self._frame,
                                  text='Login',
                                  command=self._handle_login)

        create_new_user_button = ttk.Button(master=self._frame,
                                            text='Create new user',
                                            command=self._handle_create_new_user_view)

        # build the ui

        heading_label.grid(row=0, column=0)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        create_new_user_button.grid(row=3, column=0)
        login_button.grid(row=3, column=1)
