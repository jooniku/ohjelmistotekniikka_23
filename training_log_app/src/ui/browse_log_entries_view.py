import tkinter as tk
from tkinter import ttk, constants, scrolledtext
from services.log_entry_service import log_entry_service
from ui.app_style import AppStyle


class BrowseLogEntriesView:
    '''Class for page where user can
    browse all log entries.'''

    def __init__(self, root, main_user_page, theme):
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

        self.style = AppStyle(theme=theme)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

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
                                               wraplength=60,
                                               style='text.TLabel')
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

        self.entry = log_entry_service.get_log_entry_with_id(self.current_log_id)

        self.log_entry_frame = ttk.Frame(master=self._frame,
                                        style='inner_frame.TFrame')

        self.main_label = ttk.Label(master=self._frame, text='Browse Log Entries',
                                    justify='center', style='text.TLabel')

        self.date_label = ttk.Label(
            master=self.log_entry_frame, text=f'Date:\n{self.entry[3]}',
            style='inside_text.TLabel', justify='center')

        # this is done so it won't display 'no data minutes'
        time_var = ''
        if self.entry[3] != self.entry[2]:
            time_var += f' minutes'

        self.duration_label = ttk.Label(
            master=self.log_entry_frame, text=f'Duration:\n{self.entry[4]}{time_var}',
            style='inside_text.TLabel', justify='center')
        self.session_style_label = ttk.Label(
            master=self.log_entry_frame, text=f'Session style:\n{self.entry[5]}',
            style='inside_text.TLabel', justify='center')

        self.create_text_boxes()
        self._build_log_entry_frame()


    def create_text_boxes(self):
        '''Creates text boxes for displaying possibly
        long text.
        '''
        
        labels = ['What went well:', 'What did not go well:', 'Goal for next session:']

        for text_box in range(len(labels)):
            main_label = ttk.Label(
                master=self.log_entry_frame, text=labels[text_box],
                style='inside_text.TLabel', justify='center')
            
            main_box = tk.Text(
                master=self.log_entry_frame, wrap='word',
                width=30, height=5)
            
            main_scrollbar = ttk.Scrollbar(
                self.log_entry_frame, orient='vertical',
                command=main_box.yview)
            
            main_box.config(
                yscrollcommand=main_scrollbar.set)
            
            main_box.insert('end', f'{self.entry[6+text_box]}')
            main_box.configure(state='disabled')

            main_label.grid(row=6+text_box*2, column=0, padx=10, pady=5)
            main_box.grid(row=7+text_box*2, column=0, padx=10, pady=5)


    def _build_log_entry_frame(self):
        '''place previously created objects on the window
        '''

        self.log_entry_frame.grid(
            row=1, rowspan=3, column=1, columnspan=2, padx=10, pady=10)

        self.main_label.grid(row=0, columnspan=5, pady=10)

        self.date_label.grid(row=3, column=0, padx=10, pady=5)
        self.duration_label.grid(row=4, column=0, padx=10, pady=5)
        self.session_style_label.grid(row=5, column=0, padx=10, pady=5)


    def _define_buttons(self):
        '''Display buttons for controlling page.
        '''

        previous_log_button = ttk.Button(master=self._frame,
                                         text='Previous',
                                         command=self._handle_previous_log,
                                         style='button.TButton')

        next_log_button = ttk.Button(master=self._frame,
                                     text='Next',
                                     command=self._handle_next_log,
                                     style='button.TButton')

        back_button = ttk.Button(master=self._frame,
                                 text='Back',
                                 command=self._handle_go_back,
                                 style='button.TButton')

        previous_log_button.grid(row=2, column=0, padx=5, pady=5)
        next_log_button.grid(row=2, column=4, padx=5, pady=5)
        back_button.grid(row=4, columnspan=5, pady=5)

    def _initialize(self):
        '''Initializes this page, is called
        from the __init__ function.
        '''

        self._frame = ttk.Frame(master=self._root, style='background.TFrame')

        self._define_log_entry_frame()
        self._define_buttons()
