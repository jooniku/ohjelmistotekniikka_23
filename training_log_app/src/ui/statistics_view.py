from tkinter import ttk, constants
from services.log_entry_service import log_entry_service

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


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

        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.back_button.grid(row=5, column=1, padx=5, pady=5)

        self._define_goals_achieved_frame()
        self._define_total_sessions_frame()
        self._define_training_sessions_weekly_frame()
        self._define_rank_session_styles_frame()
        self._define_training_instances_frame()

    def _create_graph_of_weekly_session_this_year(self):
        '''Creates a graph of weekly training sessions
        this year using matplotlib.
        '''

        graph_data = log_entry_service.get_weekly_user_training_instances_this_year()

        figure = Figure(figsize=(6, 3),
                        dpi=75,
                        facecolor='lightgrey',
                        layout='tight'
                        )

        ax = figure.add_subplot()

        bar = ax.bar([i for i in range(1, 53)], graph_data, color='darkred')

        ax.set_xlabel('week')
        ax.set_xlim([1, 52])
        ax.set_ylabel('sessions')
        ax.set_ylim([0, 7])

        canvas = FigureCanvasTkAgg(
            figure, master=self.training_sessions_weekly_frame)

        canvas.draw()

        canvas.get_tk_widget().configure(background='black')
        canvas.get_tk_widget().pack()

    def _define_training_sessions_weekly_frame(self):
        self.training_sessions_weekly_frame = ttk.Labelframe(master=self._frame,
                                                             text='Graph of weekly training sessions this year',
                                                             labelanchor='n')

        self._create_graph_of_weekly_session_this_year()

        self.training_sessions_weekly_frame.grid(
            row=4, column=0, columnspan=2, padx=self.padx, pady=self.pady)

    def _define_total_sessions_frame(self):
        self.total_sessions_frame = ttk.Labelframe(master=self._frame,
                                                   text='Total training sessions',
                                                   labelanchor='n')

        self.total_sessions_label = ttk.Label(master=self.total_sessions_frame,
                                              text=f'{log_entry_service.get_total_amount_of_training_sessions()}')

        self.total_sessions_frame.grid(
            row=1, column=0, padx=self.padx, pady=self.pady)
        self.total_sessions_label.grid(padx=self.padx, pady=self.pady)

    def _define_training_instances_frame(self):
        self.training_instances_frame = ttk.Labelframe(master=self._frame,
                                                       text='Training sessions this',
                                                       labelanchor='n')
        data = log_entry_service.get_current_training_instances()

        self.year_label = ttk.Label(master=self.training_instances_frame,
                                    text=f'Year: {data[0]}')
        self.month_label = ttk.Label(master=self.training_instances_frame,
                                     text=f'Month: {data[1]}')
        self.week_label = ttk.Label(master=self.training_instances_frame,
                                    text=f'Week: {data[2]}')

        self.training_instances_frame.grid(
            row=3, column=1, padx=self.padx, pady=self.pady)

        self.year_label.grid(row=1, padx=self.padx, pady=self.pady)
        self.month_label.grid(row=2, padx=self.padx, pady=self.pady)
        self.week_label.grid(row=3, padx=self.padx, pady=self.pady)

    def _define_rank_session_styles_frame(self):
        self.rank_session_styles_frame = ttk.Labelframe(master=self._frame,
                                                        text='Session styles ranked',
                                                        labelanchor='n')

        self.rank_session_styles_frame.grid(
            row=3, column=0, padx=self.padx, pady=self.pady)

        ranking_data = log_entry_service.get_users_session_styles_ranked()

        if ranking_data == []:
            info = ttk.Label(master=self.rank_session_styles_frame,
                             text='No data')
            info.grid(padx=self.padx, pady=self.pady)

        for rank in range(len(ranking_data)):
            place = ttk.Label(master=self.rank_session_styles_frame,
                              text=f'{rank+1}. {ranking_data[rank][1]}, {ranking_data[rank][0]} session(s)')
            place.grid(row=rank, column=0, padx=self.padx, pady=self.pady)

    def _define_goals_achieved_frame(self):
        self.precentage_of_goals_achieved_frame = ttk.Labelframe(master=self._frame,
                                                                 text='Precentage of goals achieved',
                                                                 labelanchor='n')
        self.goals_achieved_label = ttk.Label(master=self.precentage_of_goals_achieved_frame,
                                              text=f'{log_entry_service.get_precentage_of_goals_achieved():.0f}%')

        self.precentage_of_goals_achieved_frame.grid(
            row=1, column=1, padx=self.padx, pady=self.pady)
        self.goals_achieved_label.grid(padx=self.padx, pady=self.pady)

    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root, height=50, width=50)

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        # consists of first part defining variables and
        # second part building them
        self._define_statistics_frame()
