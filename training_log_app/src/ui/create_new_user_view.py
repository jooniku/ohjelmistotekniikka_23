from tkinter import ttk, constants
from services.log_entry_service import log_entry_service, UsernameAlreadyInUseError, InvalidInputError


class CreateNewUserView:
    '''Class for the ui of creating a new user'''

    def __init__(self, root, login_view) -> None:
        self._root = root
        self._show_login_view = login_view
        self._frame = None
        self.error_label = None

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
            self._show_login_view()

        except UsernameAlreadyInUseError:
            if self.error_label:
                self.error_label.grid_remove()
            self.error_label = ttk.Label(master=self._create_new_user_frame,
                                        text='Username already taken!',
                                        foreground='red')
            self.error_label.grid(row=3, column=0, columnspan=2)

        except InvalidInputError:
            if self.error_label:
                self.error_label.grid_remove()
            self.error_label = ttk.Label(master=self._create_new_user_frame,
                                        text='Invalid username or password!',
                                        foreground='red')
            self.error_label.grid(row=3, column=0, columnspan=2)

    def _handle_go_back(self):
        self._show_login_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text='Create new user')

        self._create_new_user_frame = ttk.Labelframe(master=self._frame,
                                                     text='Create a new user',
                                                     labelanchor='n')


        username_label = ttk.Label(master=self._create_new_user_frame, text='Username:')
        self._username_entry = ttk.Entry(master=self._create_new_user_frame)

        password_label = ttk.Label(master=self._create_new_user_frame, text='Password:')
        self._password_entry = ttk.Entry(master=self._create_new_user_frame)

        create_button = ttk.Button(master=self._frame,
                                   text='Create user',
                                   command=self._handle_create_new_user)
        
        back_button = ttk.Button(master=self._frame,
                                 text='Back',
                                 command=self._handle_go_back)

        # build the ui
        self._create_new_user_frame.grid(columnspan=2, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, padx=5, pady=5)

        create_button.grid(row=3, column=1, padx=5, pady=5)

        back_button.grid(row=3, column=0, padx=5, pady=5)