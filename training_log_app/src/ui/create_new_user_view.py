from tkinter import ttk, constants
from services.log_entry_service import log_entry_service, UsernameAlreadyInUseError, InvalidInputError
from ui.app_style import AppStyle

class CreateNewUserView:
    '''Class for the ui of creating a new user.
    '''

    def __init__(self, root, login_view, theme):
        '''initialize class

        Args:
            root: main window of app
            login_view: is returned to login page after user creation
            theme: what theme to use
        '''

        self._root = root
        self._show_login_view = login_view
        self._frame = None
        self.error_label = None

        self.style = AppStyle(theme=theme)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_new_user(self):
        '''Create a new user. This is called with create button.
        Checks if username taken and does input validation.

        If successful, go to login page.
        '''

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            log_entry_service.create_new_user(username, password)
            self._show_login_view()

        except UsernameAlreadyInUseError:
            if self.error_label:
                self.error_label.grid_remove()
            self.error_label = ttk.Label(master=self._frame,
                                         text='Username already taken!',
                                         foreground='red',
                                         style='text.TLabel')
            self.error_label.grid(row=3, column=0, columnspan=2)

        except InvalidInputError:
            if self.error_label:
                self.error_label.grid_remove()
            self.error_label = ttk.Label(master=self._frame,
                                         text='Invalid username or password!',
                                         foreground='red',
                                         style='text.TLabel')
            self.error_label.grid(row=3, column=0, columnspan=2)

    def _handle_go_back(self):
        self._show_login_view()

    def _define_create_new_user_frame(self):
        '''Creates the page for creating new user.
        '''

        self._create_new_user_frame = ttk.Frame(master=self._frame,
                                                style='login_frame.TFrame')

        main_label = ttk.Label(master=self._frame,
                               text='Create a new user',
                               style='text.TLabel',
                               justify='center')

        username_label = ttk.Label(
            master=self._create_new_user_frame, text='Username:', style='login_text.TLabel')
        self._username_entry = ttk.Entry(
            master=self._create_new_user_frame, style='input_field.TEntry')

        password_label = ttk.Label(
            master=self._create_new_user_frame, text='Password:', style='login_text.TLabel')
        self._password_entry = ttk.Entry(
            master=self._create_new_user_frame, style='input_field.TEntry')

        create_button = ttk.Button(master=self._frame,
                                   text='Create user',
                                   command=self._handle_create_new_user,
                                   style='login_button.TButton')

        back_button = ttk.Button(master=self._frame,
                                 text='Back',
                                 command=self._handle_go_back,
                                 style='login_button.TButton')

        # place the created objects on the window
        main_label.grid(row=0, columnspan=2, padx=5, pady=5)

        self._create_new_user_frame.grid(
            row=1, columnspan=2, rowspan=2, padx=25, pady=15)

        username_label.grid(row=1, column=0, padx=10, pady=10)
        self._username_entry.grid(row=1, column=1, padx=10, pady=10)

        password_label.grid(row=2, column=0, padx=10, pady=10)
        self._password_entry.grid(row=2, column=1, padx=10, pady=10)

        create_button.grid(row=4, column=1, padx=10, pady=10)

        back_button.grid(row=4, column=0, padx=10, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style='background.TFrame')

        self._define_create_new_user_frame()
