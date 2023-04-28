from tkinter import ttk, constants
from services.log_entry_service import log_entry_service


class MainUserPageView:
    '''Class for main users page interface.
    '''

    def __init__(self, root,
                 login_view,
                 new_entry_view,
                 statistics_view,
                 browse_log_entries_view):
        self._root = root
        self._frame = None
        self._login_view = login_view
        self._new_entry_view = new_entry_view
        self._statistics_view = statistics_view
        self._browse_log_entries_view = browse_log_entries_view

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

    def _handle_statistics_view(self):
        self._statistics_view()

    def _handle_browse_log_entries_view(self):
        self._browse_log_entries_view()

    def _define_last_entry_frame(self):
        '''The main frame of users latest log entry. 
        '''

        latest_entry = log_entry_service.get_last_log_entry()

        self.last_entry_label = ttk.Label(master=self._frame, justify='center',
                                          text='Last entry',
                                          style='text.TLabel',
                                          padding=(0,25,0,0))
        
        self.last_entry_label_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        self.date_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Date:\n{latest_entry[3]}',
                                                      style='inside_text.TLabel', justify='center')

        # this is done so it won't display 'no data minutes'
        time_var = ''
        if latest_entry[3] != latest_entry[2]:
            time_var += f' minutes'

        self.duration_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Duration:\n{latest_entry[4]}{time_var}',
                                                      style='inside_text.TLabel', justify='center')
        self.session_style_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Session style:\n{latest_entry[5]}',
                                                      style='inside_text.TLabel', justify='center')
        self.what_went_well_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'What went well:\n{latest_entry[6]}', wraplength=250,
                                                      style='inside_text.TLabel', justify='center')
        self.what_did_not_go_well_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'What did not go well:\n{latest_entry[7]}', wraplength=250,
                                                      style='inside_text.TLabel', justify='center')
        self.goal_for_next_session_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Goal for next session:\n{latest_entry[8]}', wraplength=250,
                                                      style='inside_text.TLabel', justify='center')

    def _define_total_time_frame(self):
        '''Creates frame for displaying total time user
        has spent training.
        '''

        self.total_time_label = ttk.Label(master=self._frame,
                                          text='Total training time',
                                          style='text.TLabel',
                                          justify='center',
                                          padding=(0,10,0,0))

        self.total_time_label_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        total_time_spent_in_minutes = log_entry_service.get_total_time_spent_training()

        self.total_time_spent_hours_label = ttk.Label(master=self.total_time_label_frame,
                                                      text=f'{total_time_spent_in_minutes / 60:.01f} hours',
                                                      style='inside_text.TLabel',
                                                      justify='center')

        self.total_time_spent_days_label = ttk.Label(master=self.total_time_label_frame,
                                                     text=f'{total_time_spent_in_minutes / (60*24):.01f} days',
                                                      style='inside_text.TLabel',
                                                      justify='center')

    def _define_nav_bar_frame(self):
        '''Creates a "nav bar" where user
        can navigate to different pages.
        '''

        self.nav_bar_frame = ttk.Frame(
            master=self._frame, padding=(0, 0, 0, 10), style='navbar.TFrame')

        self.username_label = ttk.Label(
            master=self.nav_bar_frame, text=f'Logged in as {log_entry_service.user.username}',
            style='navbar_text.TLabel')

        self.new_log_entry_button = ttk.Button(master=self.nav_bar_frame,
                                               text='New Log Entry',
                                               command=self._handle_new_entry,
                                               style='button.TButton')

        self.logout_button = ttk.Button(master=self.nav_bar_frame,
                                        text='Log out',
                                        command=self._handle_logout,
                                        style='button.TButton')

        self.statistics_view_button = ttk.Button(master=self.nav_bar_frame,
                                                text='Statistics',
                                                command=self._handle_statistics_view,
                                                style='button.TButton')

        self.browse_log_entries_view_button = ttk.Button(master=self.nav_bar_frame,
                                                text='Browse logs',
                                                command=self._handle_browse_log_entries_view,
                                                style='button.TButton')

        self.nav_bar_frame.grid(row=0)
        self.username_label.grid(row=0, column=0, padx=5, pady=2)
        self.new_log_entry_button.grid(row=0, column=2, ipadx=5, ipady=2)
        self.browse_log_entries_view_button.grid(
            row=0, column=3, ipadx=5, ipady=2)
        self.statistics_view_button.grid(row=0, column=4, ipadx=5, ipady=2)
        self.logout_button.grid(row=0, column=5, ipadx=5, ipady=2)

    def _build_total_time_frame(self):
        '''Displays the previously created frame for
        showing the total time user has spent training.
        '''

        self.total_time_label.grid(row=1)

        self.total_time_label_frame.grid(
            row=2, column=0, padx=self.padx, pady=self.pady)

        self.total_time_spent_hours_label.grid(
            row=1, column=0, padx=10, pady=5)
        self.total_time_spent_days_label.grid(
            row=2, column=0, padx=15, pady=5)

    def _build_last_entry_frame(self):
        '''Displays the latest entry frame created earlier
        on the window.
        '''

        self.last_entry_label.grid(row=3)

        self.last_entry_label_frame.grid(
            row=4, column=0, padx=10, pady=10)
        

        self.date_label.grid(row=3, column=0, padx=10, pady=5)
        self.duration_label.grid(row=4, column=0, padx=10, pady=5)
        self.session_style_label.grid(row=5, column=0, padx=10, pady=5)
        self.what_went_well_label.grid(row=6, column=0, padx=10, pady=5)
        self.what_did_not_go_well_label.grid(row=7, column=0, padx=10, pady=5)
        self.goal_for_next_session_label.grid(
            row=8, column=0, padx=10, pady=5)
    
    
    def _style_config(self):
        '''Style the page.
        '''

        self.style = ttk.Style()
    
        self.style.configure('background.TFrame', background='#2C3E50')
        self.style.configure('navbar.TFrame', background='#23313f', relief='flat')
        self.style.configure('navbar_text.TLabel', background='#23313f', foreground='#ECF0F1')
        self.style.configure('inner_frame.TFrame', background='#31404f', relief='sunken')
        self.style.configure('text.TLabel', background='#2C3E50', foreground='#ECF0F1')
        self.style.configure('inside_text.TLabel', background='#31404f', foreground='#ECF0F1')
        self.style.configure('button.TButton', background='#23313f', foreground='#ECF0F1', relief='flat')
        self.style.map('button.TButton', relief=[('active', 'ridge')], background=[('active', '#31404f')])
        self.style.configure('input_field.TEntry', background='#ECF0F1')
        

    def _initialize(self):
        '''Initialize page.
        '''

        self._frame = ttk.Frame(master=self._root, style='background.TFrame')
        self.heading_label = ttk.Label(master=self._frame, text='Main Page')

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        self._define_nav_bar_frame()
        self._define_total_time_frame()
        self._define_last_entry_frame()

        # write variables to window aka build the ui
        self._build_total_time_frame()
        self._build_last_entry_frame()
