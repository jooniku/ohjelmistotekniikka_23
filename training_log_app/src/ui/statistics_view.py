from tkinter import ttk, constants
from services.log_entry_service import log_entry_service

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


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
        '''Style the statistics page.
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

    def _handle_go_back(self):
        self._main_user_page()

    def _define_statistics_frame(self):
        '''Creates the main frame of the page.
        Also creates necessary button to go back.
        '''

        self.heading_label = ttk.Label(
            master=self._frame, text='Statistics', justify='center', style='text.TLabel', padding=(0,0,0,10))

        self.back_button = ttk.Button(
            master=self._frame, text='Back', command=self._handle_go_back, style='button.TButton')

        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.back_button.grid(row=6, column=1, padx=5, pady=5)

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
                        facecolor='#31404f',
                        layout='tight')

        ax = figure.add_subplot()

        bar = ax.bar([i for i in range(1, 53)], graph_data, color='#3498DB')

        ax.set_xlabel('week', color='#ECF0F1')
        ax.set_xlim([1, 52])
        ax.set_ylabel('sessions', color='#ECF0F1')
        ax.set_ylim([0, 7])

        canvas = FigureCanvasTkAgg(
            figure, master=self.training_sessions_weekly_frame)

        canvas.draw()

        canvas.get_tk_widget().pack()

    def _define_training_sessions_weekly_frame(self):
        '''Creates the frame where the graph of weekly sessions
        is put.
        '''
        
        self.training_sessions_weekly_frame = ttk.Labelframe(master=self._frame,
                                                             text='Graph of weekly training sessions this year',
                                                             labelanchor='n')

        self._create_graph_of_weekly_session_this_year()

        self.training_sessions_weekly_frame.grid(
            row=5, column=0, columnspan=2, padx=self.padx, pady=self.pady)

    def _define_total_sessions_frame(self):
        '''Creates a frame where total amount of sessions is displayed.
        '''

        self.total_sessions_frame = ttk.Frame(master=self._frame, style='inner_frame.TFrame')

        self.total_sessions_label = ttk.Label(master=self._frame,
                                              text='Total training sessions',
                                              style='text.TLabel',
                                              justify='center',
                                              padding=(0,10,0,0))
        
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
            row=4, column=1, padx=self.padx, pady=self.pady)

        self.year_label.grid(row=1, padx=self.padx, pady=self.pady)
        self.month_label.grid(row=2, padx=self.padx, pady=self.pady)
        self.week_label.grid(row=3, padx=self.padx, pady=self.pady)

    def _define_rank_session_styles_frame(self):
        '''Creates a frame where session styles are ranked by
        how many times user has trained in them.
        '''

        self.rank_session_styles_frame = ttk.Labelframe(master=self._frame,
                                                        text='Session styles ranked',
                                                        labelanchor='n')

        self.rank_session_styles_frame.grid(
            row=4, column=0, padx=self.padx, pady=self.pady)

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
        '''Creates frame which displays the precentage of goals user has achieved.
        '''
        
        self.precentage_of_goals_achieved_frame = ttk.Frame(master=self._frame, style='inner_frame.TFrame')
        self.precentage_of_goals_achieved_label = ttk.Label(master=self._frame,
                                                            text='Precentage of goals achieved',
                                                            justify='center',
                                                            style='text.TLabel',
                                                            padding=(0,10,0,0))

        self.goals_achieved_label = ttk.Label(master=self.precentage_of_goals_achieved_frame,
                                              text=f'{log_entry_service.get_precentage_of_goals_achieved():.0f}%',
                                              style='inside_text.TLabel')

        self.precentage_of_goals_achieved_label.grid(row=1, column=1)

        self.precentage_of_goals_achieved_frame.grid(
            row=2, column=1, padx=10, pady=10)
        
        self.goals_achieved_label.grid(padx=10, pady=10)

    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root, style='background.TFrame')

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        # consists of first part defining variables and
        # second part building them
        self._define_statistics_frame()
