from tkinter import ttk, constants
from services.log_entry_service import log_entry_service


class BrowseLogEntriesView:
    '''Class for page where user can
    browse all log entries.'''

    def __init__(self, root, main_user_page):
        '''Initialize class.

        Args:
            root: main window frame
            main_user_page: user can go back to main page
        '''

        self._root = root
        self._frame = None
        self._main_user_page = main_user_page

        self.current_log_id = log_entry_service.get_latest_log_id()
        self.max_log_id = self.current_log_id
        self.log_index_error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _style_config(self):
        '''Style the current page.
        '''

        self.style = ttk.Style()

        self.style.configure('label_frame.TLabelFrame', background='red')

    def _handle_go_back(self):
        self._main_user_page()

    def _handle_next_log(self):
        '''When "next" button is pressed this function is called.
        Calls self._define_log_entry_frame() for next log.
        '''

        if self.log_index_error_label:
            self.log_index_error_label.grid_remove()

        if self.current_log_id is not None and self.current_log_id < self.max_log_id:
            self.current_log_id += 1
            self.log_entry_frame.grid_forget()
            self._define_log_entry_frame()
        else:
            self._handle_log_index_error('Already latest entry!', 4)

    def _handle_log_index_error(self, message, columnpos):
        '''If already at latest or first log entry and user tries
        to go to even more recent entry (which doesn't exist) etc.,
        this function promts message to user about it.

        Args:
            message: what (error)message to show
            columnpos: which column in tkinter window to show message
        '''

        if self.log_index_error_label:
            self.log_index_error_label.grid_remove()
        self.log_index_error_label = ttk.Label(master=self._frame,
                                               text=message,
                                               foreground='red',
                                               wraplength=60)
        self.log_index_error_label.grid(row=0, rowspan=2, column=columnpos)

    def _handle_previous_log(self):
        '''When "previous" button is pressed this function is called.
        Calls self._define_log_entry_frame() for previous log.
        '''

        if self.log_index_error_label:
            self.log_index_error_label.grid_remove()

        if self.current_log_id is not None and self.current_log_id > 1:
            self.current_log_id -= 1
            self.log_entry_frame.grid_forget()
            self._define_log_entry_frame()
        else:
            self._handle_log_index_error('No previous entries!', 0)

    def _define_log_entry_frame(self):
        '''The main frame of log entry being displayed. 
        Grabs an entry by id and displays it.

        Is a bit long, but it performs one task and it's easier
        to read it in it's current structure rather than chopped up.
        '''

        entry = log_entry_service.get_log_entry_with_id(self.current_log_id)

        self.log_entry_frame = ttk.LabelFrame(master=self._frame)
        self.main_label = ttk.Label(master=self._frame, text='Browse Log Entries',
                                    justify='center')

        self.date_label = ttk.Label(
            master=self.log_entry_frame, text=f'Date: {entry[3]}')

        # this is done so it won't display 'no data minutes'
        time_var = ''
        if entry[3] != entry[2]:
            time_var += f' minutes'

        self.duration_label = ttk.Label(
            master=self.log_entry_frame, text=f'Duration: {entry[4]}{time_var}')
        self.session_style_label = ttk.Label(
            master=self.log_entry_frame, text=f'Session style: {entry[5]}')
        self.what_went_well_label = ttk.Label(
            master=self.log_entry_frame, text=f'What went well: {entry[6]}', wraplength=300)
        self.what_did_not_go_well_label = ttk.Label(
            master=self.log_entry_frame, text=f'What did not go well: {entry[7]}', wraplength=300)
        self.goal_for_next_session_label = ttk.Label(
            master=self.log_entry_frame, text=f'Goal for next session: {entry[8]}', wraplength=300)

        # place previously created objects on the window
        self.log_entry_frame.grid(
            row=1, rowspan=3, column=1, columnspan=2, padx=10, pady=10)

        self.main_label.grid(row=0, columnspan=5, pady=10)

        self.date_label.grid(row=3, column=0, ipadx=5, ipady=5)
        self.duration_label.grid(row=4, column=0, ipadx=5, ipady=5)
        self.session_style_label.grid(row=5, column=0, ipadx=5, ipady=5)
        self.what_went_well_label.grid(row=6, column=0, ipadx=5, ipady=5)
        self.what_did_not_go_well_label.grid(row=7, column=0, ipadx=5, ipady=5)
        self.goal_for_next_session_label.grid(
            row=8, column=0, ipadx=5, ipady=5)

    def _define_buttons(self):
        '''Display buttons for controlling page.
        '''

        previous_log_button = ttk.Button(master=self._frame,
                                         text='Previous',
                                         command=self._handle_previous_log)

        next_log_button = ttk.Button(master=self._frame,
                                     text='Next',
                                     command=self._handle_next_log)

        back_button = ttk.Button(master=self._frame,
                                 text='Back',
                                 command=self._handle_go_back)

        previous_log_button.grid(row=2, column=0, padx=5, pady=5)
        next_log_button.grid(row=2, column=4, padx=5, pady=5)
        back_button.grid(row=4, columnspan=5, pady=5)

    def _initialize(self):
        '''Initializes this page, is called
        from the __init__ function.'''

        self._frame = ttk.Frame(master=self._root)

        self._style_config()
        self._define_log_entry_frame()
        self._define_buttons()

        self.padx = 10
        self.pady = 10
