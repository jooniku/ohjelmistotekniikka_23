from tkinter import ttk, constants
from services.log_entry_service import log_entry_service


class StatisticsPageView:
    '''Class for main users page interface'''

    def __init__(self, root, main_user_page):
        self._root = root
        self._frame = None
        self._main_user_page = main_user_page

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout(self):
        log_entry_service.logout()
        self._login_view()

    def _style_config(self):
        # style the window, currently doesn't work

        self.style = ttk.Style()

        self.style.configure('label_frame.TLabelFrame', background='red')

    def _handle_go_back(self):
        self._main_user_page()

    def _define_statistics_frame(self):
        self.heading_label = ttk.Label(
            master=self._frame, text='Statistics', justify='center')
        
        self.back_button = ttk.Button(
            master=self._frame, text='Back', command=self._handle_go_back)

        self._define_goals_achieved_frame()
        self._define_total_sessions_frame()
        self._define_rank_session_styles_frame()

    def _define_total_sessions_frame(self):
        self.total_sessions_frame = ttk.Labelframe(master=self._frame,
                                                   text='Total training sessions',
                                                   labelanchor='n')

        self.total_sessions_label = ttk.Label(master=self.total_sessions_frame,
                                              text=f'{log_entry_service.get_total_amount_of_training_sessions()}')

    def _define_rank_session_styles_frame(self):
        self.rank_session_styles_frame = ttk.Labelframe(master=self._frame,
                                                        text='Session styles ranked',
                                                        labelanchor='n')

    def _define_goals_achieved_frame(self):
        self.precentage_of_goals_achieved_frame = ttk.Labelframe(master=self._frame,
                                                                 text='Precentage of goals achieved',
                                                                 labelanchor='n')
        self.goals_achieved_label = ttk.Label(master=self.precentage_of_goals_achieved_frame,
                                              text=f'{log_entry_service.get_precentage_of_goals_achieved():.0f}%')

    def _build_total_sessions_frame(self):
        self.total_sessions_frame.grid(
            row=1, column=0, padx=self.padx, pady=self.pady)
        self.total_sessions_label.grid(padx=self.padx, pady=self.pady)

    def _build_goals_achieved_frame(self):
        self.precentage_of_goals_achieved_frame.grid(
            row=2, column=0, padx=self.padx, pady=self.pady)
        self.goals_achieved_label.grid(padx=self.padx, pady=self.pady)

    def _build_statistics_frame(self):
        self.heading_label.grid(row=0, column=0)
        self.back_button.grid(row=4, column=0)

        self._build_total_sessions_frame()
        self._build_goals_achieved_frame()

    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root, height=50, width=50)

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        self._define_statistics_frame()

        # write variables to window aka build the ui
        self._build_statistics_frame()
