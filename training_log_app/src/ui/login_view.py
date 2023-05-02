from tkinter import ttk, constants
from services.log_entry_service import log_entry_service, InvalidCredentialsError
from ui.app_style import AppStyle

class LoginView:
    '''Class responsible for login page UI
    '''

    def __init__(self, root, show_main_page, show_create_new_user, theme):
        self._root = root
        self._show_main_page = show_main_page
        self._show_create_new_user = show_create_new_user


        self.style = AppStyle(theme)

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        '''Handles logging user in. Is called with log in button.
        If wrong username etc. prompts user with message.
        '''

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            log_entry_service.login(username, password)
            self._show_main_page()

        except InvalidCredentialsError:
            error_label = ttk.Label(master=self._frame,
                                    text='Wrong username or password!',
                                    foreground='red',
                                    style='text.TLabel')
            error_label.grid(row=3, column=0, columnspan=2)

    def _handle_create_new_user_view(self):
        '''Shows the page for creating new user.
        '''

        self._show_create_new_user()

    def _define_login_frame(self):
        '''Creates the login page. 
        '''

        self.login_frame_label = ttk.Frame(
            master=self._frame,
            style='login_frame.TFrame')

        self.login_label = ttk.Label(master=self._frame,
                                     text='Log in or create a new user',
                                     style='text.TLabel',
                                     justify='center')

        self.username_label = ttk.Label(
            master=self.login_frame_label, text='Username:', style='login_text.TLabel')
        self._username_entry = ttk.Entry(
            master=self.login_frame_label, style='input_field.TEntry')

        self.password_label = ttk.Label(
            master=self.login_frame_label, text='Password:', style='login_text.TLabel')
        self._password_entry = ttk.Entry(
            master=self.login_frame_label, style='input_field.TEntry')

        self.login_label.grid(row=0, columnspan=2, padx=5, pady=5)

        self.login_frame_label.grid(
            row=1, column=0, columnspan=2, padx=25, pady=15, rowspan=2)

        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self._username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self._password_entry.grid(row=2, column=1, padx=10, pady=10)

    def _define_buttons(self):
        '''Create the buttons on the login page.
        '''

        self.login_button = ttk.Button(master=self._frame,
                                       text='Login',
                                       command=self._handle_login,
                                       style='login_button.TButton')

        self.create_new_user_button = ttk.Button(master=self._frame,
                                                 text='Create new user',
                                                 command=self._handle_create_new_user_view,
                                                 style='login_button.TButton')

        self.create_new_user_button.grid(
            row=4, column=0, columnspan=1, padx=5, pady=5)
        self.login_button.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

    def _initialize(self):
        '''This is called from __init__ function.
        Calls functions to create page.
        '''

        self._frame = ttk.Frame(master=self._root, style='background.TFrame')

        self._define_login_frame()
        self._define_buttons()
