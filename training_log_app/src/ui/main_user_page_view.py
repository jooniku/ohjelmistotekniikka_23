import tkinter as tk
from tkinter import ttk, constants
from services.log_entry_service import log_entry_service
from ui.app_style import AppStyle


class MainUserPageView:
    '''Class for main users page interface.
    '''

    def __init__(self, root,
                 login_view,
                 new_entry_view,
                 statistics_view,
                 browse_log_entries_view,
                 change_theme,
                 theme):
        '''Initialize view.

        Args:
            root: root window
            login_view (method):  method to go to this page
            new_entry_view (method):  method to go to this page
            statistics_view (method): method to go to this page
            browse_log_entries_view (method): method to go to this page
            change_theme (method): method to change theme globally
            theme (string): which theme to use
        '''

        self._root = root
        self._frame = None
        self._login_view = login_view
        self._new_entry_view = new_entry_view
        self._statistics_view = statistics_view
        self._browse_log_entries_view = browse_log_entries_view
        self._change_theme = change_theme
        self._theme = theme

        self.style = AppStyle(theme=self._theme)

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

    def _handle_change_theme(self):
        self._change_theme()

    def _define_last_entry_frame(self):
        '''The main frame of users latest log entry. 
        '''

        self.latest_entry = log_entry_service.get_last_log_entry()

        self.last_entry_label = ttk.Label(master=self._frame, justify='center',
                                          text='Last entry',
                                          style='text.TLabel',
                                          padding=(0, 25, 0, 0))

        self.last_entry_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        self.date_label = ttk.Label(
            master=self.last_entry_frame, text=f'Date:\n{self.latest_entry[3]}',
            style='inside_text.TLabel', justify='center')

        # this is done so it won't display 'no data minutes'
        time_var = ''
        if self.latest_entry[3] != self.latest_entry[2]:
            time_var += f' minutes'

        self.duration_label = ttk.Label(
            master=self.last_entry_frame, text=f'Duration:\n{self.latest_entry[4]}{time_var}',
            style='inside_text.TLabel', justify='center')
        self.session_style_label = ttk.Label(
            master=self.last_entry_frame, text=f'Session style:\n{self.latest_entry[5]}',
            style='inside_text.TLabel', justify='center')
        
        self.create_text_boxes()

    def create_text_boxes(self):
        '''Creates text boxes for displaying possibly
        long text.
        '''
        
        labels = ['What went well:', 'What did not go well:', 'Goal for next session:']

        for text_box in range(len(labels)):
            main_label = ttk.Label(
                master=self.last_entry_frame, text=labels[text_box],
                style='inside_text.TLabel', justify='center')
            
            main_box = tk.Text(
                master=self.last_entry_frame, wrap='word',
                width=30, height=5)
            
            main_scrollbar = ttk.Scrollbar(
                self.last_entry_frame, orient='vertical',
                command=main_box.yview)
            
            main_box.config(
                yscrollcommand=main_scrollbar.set)
            
            main_box.insert('end', f'{self.latest_entry[6+text_box]}')
            main_box.configure(state='disabled')

            main_label.grid(row=6+text_box*2, column=0, padx=10, pady=5)
            main_box.grid(row=7+text_box*2, column=0, padx=10, pady=5)


    def _define_total_time_frame(self):
        '''Creates frame for displaying total time user
        has spent training.
        '''

        self.total_time_label = ttk.Label(master=self._frame,
                                          text='Total training time',
                                          style='text.TLabel',
                                          justify='center',
                                          padding=(0, 10, 0, 0))

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
            master=self._frame, padding=(0, 0, 0, 4), style='navbar.TFrame')

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

        self.change_theme_button = ttk.Button(master=self.nav_bar_frame,
                                              text='Change theme',
                                              style='button.TButton',
                                              command=self._handle_change_theme)

        self.nav_bar_frame.grid(row=0)
        self.username_label.grid(row=0, column=0, padx=5, pady=2)
        self.new_log_entry_button.grid(row=0, column=2, ipadx=5, ipady=2)
        self.browse_log_entries_view_button.grid(
            row=0, column=3, ipadx=5, ipady=2)
        self.statistics_view_button.grid(row=0, column=4, ipadx=5, ipady=2)
        self.change_theme_button.grid(row=0, column=5, ipadx=5, ipady=2)
        self.logout_button.grid(row=0, column=6, ipadx=5, ipady=2)

    def _build_total_time_frame(self):
        '''Displays the previously created frame for
        showing the total time user has spent training.
        '''

        self.total_time_label.grid(row=1)

        self.total_time_label_frame.grid(
            row=2, column=0, padx=10, pady=10)

        self.total_time_spent_hours_label.grid(
            row=1, column=0, padx=10, pady=5)
        self.total_time_spent_days_label.grid(
            row=2, column=0, padx=15, pady=5)

    def _build_last_entry_frame(self):
        '''Displays the latest entry frame created earlier
        on the window.
        '''

        self.last_entry_label.grid(row=3)

        self.last_entry_frame.grid(
            row=4, column=0, padx=10, pady=10)

        self.date_label.grid(row=3, column=0, padx=10, pady=5)
        self.duration_label.grid(row=4, column=0, padx=10, pady=5)
        self.session_style_label.grid(row=5, column=0, padx=10, pady=5)

    def _initialize(self):
        '''Initialize page.
        '''

        self._frame = ttk.Frame(master=self._root, style='background.TFrame')
        self.heading_label = ttk.Label(master=self._frame, text='Main Page')

        # define variables and get values from database etc.
        self._define_nav_bar_frame()
        self._define_total_time_frame()
        self._define_last_entry_frame()

        # write variables to window aka build the ui
        self._build_total_time_frame()
        self._build_last_entry_frame()
