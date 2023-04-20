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

    def _define_login_frame(self):
        self.login_frame_label = ttk.Labelframe(master=self._frame, labelanchor='n', text='Log in or create a new user')

        self.username_label = ttk.Label(master=self.login_frame_label, text='Username:')
        self._username_entry = ttk.Entry(master=self.login_frame_label)

        self.password_label = ttk.Label(master=self.login_frame_label, text='Password:')
        self._password_entry = ttk.Entry(master=self.login_frame_label)

        
    def _build_login_frame(self):
        # build the ui
        self.login_frame_label.grid(row=0, column=0, padx=self.padx, pady=self.pady, rowspan=2)

        self.username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, padx=5, pady=5)


    def _define_buttons(self):
        self.login_button = ttk.Button(master=self._frame,
                                  text='Login',
                                  command=self._handle_login)

        self.create_new_user_button = ttk.Button(master=self._frame,
                                            text='Create new user',
                                            command=self._handle_create_new_user_view)

    def _build_buttons(self):
        self.create_new_user_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.login_button.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root)

        self.padx = 10
        self.pady = 10

        self._define_login_frame()
        self._define_buttons()

        self._build_login_frame()
        self._build_buttons()

        
