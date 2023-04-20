from tkinter import ttk, constants, OptionMenu, StringVar
from services.log_entry_service import log_entry_service


class NewLogEntryView:
    '''UI view for adding a log entry'''

    def __init__(self, root, main_view) -> None:
        self._root = root
        self._frame = None
        self._main_user_view = main_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_new_log_entry(self):
        # call log entry service and create entry
        date = self._date_entry.get()
        duration = self._duration_entry.get()
        session_style = self._session_style_entry.get()
        what_went_well = self._whatwent_well_entry.get()
        what_did_not_go_well = self._whatdid_not_go_well_entry.get()
        goal_for_next_session = self._goal_for_next_session_entry.get()
        was_last_goal_achieved = self._was_last_goal_achieved.get()

        content = {'date': date, 'duration': duration, 'session_style': session_style,
                   'what_went_well': what_went_well,
                   'what_did_not_go_well': what_did_not_go_well,
                   'goal_for_next_session': goal_for_next_session,
                   'was_last_goal_achieved': was_last_goal_achieved}

        if content['session_style'] != 'must choose one':  # can't spam entries
            log_entry_service.create_log_entry(content=content)
            self._main_user_view()
            # mabye call a function to let user know creation was ok

    def _handle_go_back(self):
        self._main_user_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text='Add new log entry')

        # currently saves as text, create actual date entry way
        date_label = ttk.Label(master=self._frame, text='Date')
        self._date_entry = ttk.Entry(master=self._frame)

        duration_label = ttk.Label(master=self._frame, text='Duration (min)')
        self._duration_entry = ttk.Entry(master=self._frame)

        session_style_label = ttk.Label(
            master=self._frame, text='Main focus of the session')
        style_options = ['wrestling', 'grappling',
                         'striking', 'sparring', 'other']
        self._session_style_entry = StringVar(self._frame)
        self._session_style_entry.set('must choose one')  # our default value
        
        opt_session = OptionMenu(
            self._frame, self._session_style_entry, *style_options)

        whatwent_well_label = ttk.Label(
            master=self._frame, text='What went well?')
        self._whatwent_well_entry = ttk.Entry(master=self._frame)

        whatdid_not_go_well_label = ttk.Label(
            master=self._frame, text='What did not go well?')
        self._whatdid_not_go_well_entry = ttk.Entry(master=self._frame)

        goal_for_next_session_label = ttk.Label(
            master=self._frame, text='Goal for next session')
        self._goal_for_next_session_entry = ttk.Entry(master=self._frame)

        previously_set_goal = log_entry_service.get_last_entry_goal()
        prev_set_goal_label = ttk.Label(
            master=self._frame, text=f'Previously set goal: {previously_set_goal}')

        self._was_last_goal_achieved = StringVar()

        last_goal_achieved_label = ttk.Label(
            master=self._frame, text='Was last goal achieved?')

        # radio choice
        values = (('yes', True), ('no', False))
        i = 1
        for value in values:
            rad_but = ttk.Radiobutton(
                master=self._frame, text=value[0], value=value[1], variable=self._was_last_goal_achieved)
            rad_but.grid(row=8, column=i)
            i += 1

        # build the ui
        date_label.grid(row=1, column=0)
        self._date_entry.grid(row=1, column=1)

        duration_label.grid(row=2, column=0)
        self._duration_entry.grid(row=2, column=1)

        session_style_label.grid(row=3, column=0)
        opt_session.grid(row=3, column=1, columnspan=2)

        whatwent_well_label.grid(row=4, column=0)
        self._whatwent_well_entry.grid(row=4, column=1)

        whatdid_not_go_well_label.grid(row=5, column=0)
        self._whatdid_not_go_well_entry.grid(row=5, column=1)

        goal_for_next_session_label.grid(row=6, column=0)
        self._goal_for_next_session_entry.grid(row=6, column=1)

        prev_set_goal_label.grid(row=7, column=0)
        last_goal_achieved_label.grid(row=8, column=0)

        go_back_button = ttk.Button(
            master=self._frame,
            text='Go back',
            command=self._handle_go_back
        )

        save_entry_button = ttk.Button(
            master=self._frame,
            text='Save entry',
            command=self._handle_create_new_log_entry
        )

        heading_label.grid(row=0, column=0)

        save_entry_button.grid(row=9, column=1)
        go_back_button.grid(row=9, column=0)
