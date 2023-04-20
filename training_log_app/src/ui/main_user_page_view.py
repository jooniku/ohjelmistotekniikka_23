from tkinter import ttk, constants
from services.log_entry_service import log_entry_service


class MainUserPageView:
    '''Class for main users page interface'''

    def __init__(self, root, login_view, new_entry_view, statistics_view):
        self._root = root
        self._frame = None
        self._login_view = login_view
        self._new_entry_view = new_entry_view
        self._statistics_view = statistics_view

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

    def _define_last_entry_frame(self):
        latest_entry = log_entry_service.get_last_log_entry()

        self.last_entry_label_frame = ttk.Labelframe(
            master=self._frame, labelanchor='n', text='Last entry')

        self.date_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Date: {latest_entry[2]}')
        self.duration_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Duration: {latest_entry[3]} minutes')
        self.session_style_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Session style: {latest_entry[4]}')
        self.what_went_well_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'What went well: {latest_entry[5]}', wraplength=300)
        self.what_did_not_go_well_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'What did not go well: {latest_entry[6]}', wraplength=300)
        self.goal_for_next_session_label = ttk.Label(
            master=self.last_entry_label_frame, text=f'Goal for next session: {latest_entry[7]}', wraplength=300)

    def _define_total_time_frame(self):
        self.total_time_label_frame = ttk.Labelframe(
            master=self._frame, labelanchor='n', text='Total training time')

        total_time_spent_in_minutes = log_entry_service.get_total_time_spent_training()

        self.total_time_spent_hours_label = ttk.Label(master=self.total_time_label_frame,
                                                      text=f'{total_time_spent_in_minutes / 60:.01f} hours')

        self.total_time_spent_days_label = ttk.Label(master=self.total_time_label_frame,
                                                     text=f'{total_time_spent_in_minutes / (60*24):.01f} days')

    def _define_nav_bar_frame(self):
        self.nav_bar_frame = ttk.Frame(
            master=self._frame, padding=(0, 0, 0, self.pady))

        self.username_label = ttk.Label(
            master=self.nav_bar_frame, text=f'Logged in as {log_entry_service.user.username}')

        self.new_log_entry_button = ttk.Button(master=self.nav_bar_frame,
                                               text='New Log Entry',
                                               command=self._handle_new_entry)

        self.logout_button = ttk.Button(master=self.nav_bar_frame,
                                        text='Log out',
                                        command=self._handle_logout)

        self.statistics_view_button = ttk.Button(master=self.nav_bar_frame,
                                                 text='Statistics',
                                                 command=self._handle_statistics_view)

    def _build_total_time_frame(self):
        self.total_time_label_frame.grid(
            row=1, column=0, padx=self.padx, pady=self.pady)

        self.total_time_spent_hours_label.grid(
            row=1, column=0, padx=self.padx, pady=self.pady-2)
        self.total_time_spent_days_label.grid(
            row=2, column=0, padx=self.padx, pady=self.pady-2)

    def _build_last_entry_frame(self):
        self.last_entry_label_frame.grid(
            row=3, column=0, padx=self.padx, pady=self.pady)

        self.date_label.grid(row=3, column=0, ipadx=5, ipady=5)
        self.duration_label.grid(row=4, column=0, ipadx=5, ipady=5)
        self.session_style_label.grid(row=5, column=0, ipadx=5, ipady=5)
        self.what_went_well_label.grid(row=6, column=0, ipadx=5, ipady=5)
        self.what_did_not_go_well_label.grid(row=7, column=0, ipadx=5, ipady=5)
        self.goal_for_next_session_label.grid(
            row=8, column=0, ipadx=5, ipady=5)

    def _build_nav_bar_frame(self):
        self.nav_bar_frame.grid(row=0, column=0)

        self.username_label.grid(row=0, column=0, ipadx=5, ipady=1)
        self.new_log_entry_button.grid(row=0, column=2, ipadx=5, ipady=1)
        self.statistics_view_button.grid(row=0, column=3, ipadx=5, ipady=1)
        self.logout_button.grid(row=0, column=4, ipadx=5, ipady=1)

    def _style_config(self):
        # style the window, currently doesn't work

        self.style = ttk.Style()

        self.style.configure('label_frame.TLabelFrame', background='red')

    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root)
        self.heading_label = ttk.Label(master=self._frame, text='Main Page')

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        self._define_nav_bar_frame()
        self._define_total_time_frame()
        self._define_last_entry_frame()

        # write variables to window aka build the ui
        self._build_nav_bar_frame()
        self._build_total_time_frame()
        self._build_last_entry_frame()
