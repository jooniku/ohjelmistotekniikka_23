from tkinter import ttk, constants
from services.log_entry_service import log_entry_service
from ui.app_style import AppStyle

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


class StatisticsPageView:
    '''Class for main users page interface'''

    def __init__(self, root, main_user_page, theme):
        '''Initialize the page.

        Args:
            root: root window
            main_user_page (method): page to go back to
            theme (string): which theme to use
        '''

        self._root = root
        self._frame = None
        self._main_user_page = main_user_page

        self.style = AppStyle(theme=theme)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_go_back(self):
        self._main_user_page()

    def _define_statistics_frame(self):
        '''Creates the main frame of the page.
        Also creates necessary button to go back.
        '''

        self.heading_label = ttk.Label(
            master=self._frame, text='Statistics', justify='center', style='text.TLabel', padding=(0, 0, 0, 10))

        self.back_button = ttk.Button(
            master=self._frame, text='Back', command=self._handle_go_back, style='button.TButton')

        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.back_button.grid(row=7, column=1, padx=5, pady=5)

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
                        dpi=80,
                        facecolor=self.style.get_inner_frame_colour(),
                        layout='tight')

        ax = figure.add_subplot()

        bar = ax.bar([i for i in range(1, 53)], graph_data,
                     color=self.style.get_graph_bar_colour())

        ax.set_xlabel('week', color=self.style.get_inner_frame_text_colour())
        ax.set_xlim([1, 52])
        ax.set_ylabel(
            'sessions', color=self.style.get_inner_frame_text_colour())
        ax.set_ylim([0, 7])

        canvas = FigureCanvasTkAgg(
            figure, master=self.training_sessions_weekly_frame)

        canvas.draw()

        canvas.get_tk_widget().pack()

    def _define_training_sessions_weekly_frame(self):
        '''Creates the frame where the graph of weekly sessions
        is put.
        '''

        training_sessions_weekly_label = ttk.Label(master=self._frame,
                                                   text='Graph of weekly training sessions this year',
                                                   style='text.TLabel',
                                                   padding=(0, 10, 0, 0),
                                                   justify='center')

        self.training_sessions_weekly_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame', border=1)

        self._create_graph_of_weekly_session_this_year()

        training_sessions_weekly_label.grid(row=5, columnspan=2)
        self.training_sessions_weekly_frame.grid(
            row=6, column=0, columnspan=2, padx=10, pady=10)

    def _define_total_sessions_frame(self):
        '''Creates a frame where total amount of sessions is displayed.
        '''

        self.total_sessions_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        self.total_sessions_label = ttk.Label(master=self._frame,
                                              text='Total training sessions',
                                              style='text.TLabel',
                                              justify='center',
                                              padding=(0, 10, 0, 0))

        self.total_sessions_label_num = ttk.Label(master=self.total_sessions_frame,
                                                  text=f'{log_entry_service.get_total_amount_of_training_sessions()}',
                                                  style='inside_text.TLabel',
                                                  justify='center')

        self.total_sessions_label.grid(row=1, column=0)

        self.total_sessions_frame.grid(row=2, column=0, padx=10, pady=10)
        self.total_sessions_label_num.grid(padx=10, pady=10)

    def _define_training_instances_frame(self):
        '''Creates a frame where training sessions this week, month and year
        are displayed.
        '''

        training_instances_label = ttk.Label(master=self._frame,
                                             text='Training instances',
                                             style='text.TLabel',
                                             justify='center',
                                             padding=(0, 10, 0, 0))

        self.training_instances_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        data = log_entry_service.get_current_training_instances()

        self.year_label = ttk.Label(master=self.training_instances_frame,
                                    text=f'This year:\n{data[0]}',
                                    justify='center', style='inside_text.TLabel')
        self.month_label = ttk.Label(master=self.training_instances_frame,
                                     text=f'This month:\n{data[1]}',
                                     justify='center', style='inside_text.TLabel')
        self.week_label = ttk.Label(master=self.training_instances_frame,
                                    text=f'This week:\n{data[2]}',
                                    justify='center', style='inside_text.TLabel')

        training_instances_label.grid(row=3, column=1)

        self.training_instances_frame.grid(
            row=4, column=1, padx=10, pady=10)

        self.year_label.grid(row=1, padx=10, pady=10)
        self.month_label.grid(row=2, padx=10, pady=10)
        self.week_label.grid(row=3, padx=10, pady=10)

    def _define_rank_session_styles_frame(self):
        '''Creates a frame where session styles are ranked by
        how many times user has trained in them.
        '''

        rank_session_styles_label = ttk.Label(master=self._frame,
                                              text='Session styles ranked',
                                              padding=(0, 10, 0, 0),
                                              justify='center',
                                              style='text.TLabel')

        self.rank_session_styles_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')

        rank_session_styles_label.grid(row=3, column=0)
        self.rank_session_styles_frame.grid(
            row=4, column=0, padx=10, pady=10)

        ranking_data = log_entry_service.get_users_session_styles_ranked()

        if ranking_data == []:
            info = ttk.Label(master=self.rank_session_styles_frame,
                             text='No data',
                             style='inside_text.TLabel')
            info.grid(padx=10, pady=10)

        for rank in range(len(ranking_data)):
            place = ttk.Label(master=self.rank_session_styles_frame,
                              text=f'{rank+1}. {ranking_data[rank][1]}, {ranking_data[rank][0]} session(s)',
                              style='inside_text.TLabel')
            place.grid(row=rank, column=0, padx=10, pady=10)

    def _define_goals_achieved_frame(self):
        '''Creates frame which displays the precentage of goals user has achieved.
        '''

        self.precentage_of_goals_achieved_frame = ttk.Frame(
            master=self._frame, style='inner_frame.TFrame')
        self.precentage_of_goals_achieved_label = ttk.Label(master=self._frame,
                                                            text='Precentage of goals achieved',
                                                            justify='center',
                                                            style='text.TLabel',
                                                            padding=(0, 10, 0, 0))

        self.goals_achieved_label = ttk.Label(master=self.precentage_of_goals_achieved_frame,
                                              text=f'{log_entry_service.get_precentage_of_goals_achieved():.0f}%',
                                              style='inside_text.TLabel')

        self.precentage_of_goals_achieved_label.grid(row=1, column=1)

        self.precentage_of_goals_achieved_frame.grid(
            row=2, column=1, padx=10, pady=10)

        self.goals_achieved_label.grid(padx=10, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style='background.TFrame')

        self._define_statistics_frame()
