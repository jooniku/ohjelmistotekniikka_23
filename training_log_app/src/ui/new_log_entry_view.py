from tkinter import ttk, constants, OptionMenu, StringVar
from tkcalendar import DateEntry
from datetime import datetime
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
        what_went_well = self._what_went_well_entry.get()
        what_did_not_go_well = self._what_did_not_go_well_entry.get()
        goal_for_next_session = self._goal_for_next_session_entry.get()
        was_last_goal_achieved = self._was_last_goal_achieved.get()

        content = {'date': date, 'duration': duration, 'session_style': session_style,
                   'what_went_well': what_went_well,
                   'what_did_not_go_well': what_did_not_go_well,
                   'goal_for_next_session': goal_for_next_session,
                   'was_last_goal_achieved': was_last_goal_achieved}

        log_entry_service.create_log_entry(content=content)
        self._main_user_view()

    def _handle_go_back(self):
        self._main_user_view()

    def _define_date_frame(self):
        self._date_frame = ttk.Labelframe(master=self._frame,
                                          text='Date',
                                          labelanchor='nw',
                                          padding=5)

        date = datetime.today()
        self._date_entry = DateEntry(master=self._date_frame, date_pattern='dd/mm/yyyy', day=date.day, month=date.month, year=date.year,
                                     background='darkred', foreground='white', _downarrow_name='')

    def _define_duration_frame(self):
        self._duration_frame = ttk.Labelframe(master=self._frame,
                                              text='Duration (min)',
                                              labelanchor='nw',
                                              padding=5)

        self._duration_entry = ttk.Entry(master=self._duration_frame)

    def _define_session_style_frame(self):
        self._session_style_frame = ttk.Labelframe(master=self._frame,
                                                   text='Session style',
                                                   labelanchor='nw',
                                                   padding=5)

        style_options = ['wrestling', 'grappling',
                         'striking', 'sparring', 'other']

        self._session_style_entry = StringVar(self._frame)
        self._session_style_entry.set('select')  # our default value

        self.opt_session = OptionMenu(self._session_style_frame,
                                      self._session_style_entry,
                                      *style_options)

    def _define_what_went_well_frame(self):
        self._what_went_well_frame = ttk.Labelframe(master=self._frame,
                                                    text='What went well',
                                                    labelanchor='nw',
                                                    padding=5)
        self._what_went_well_entry = ttk.Entry(
            master=self._what_went_well_frame)

    def _define_what_did_not_go_well(self):
        self._what_did_not_go_well_frame = ttk.Labelframe(master=self._frame,
                                                          text='What did not go well',
                                                          labelanchor='nw',
                                                          padding=5)
        self._what_did_not_go_well_entry = ttk.Entry(
            master=self._what_did_not_go_well_frame)

    def _define_goal_for_next_session_frame(self):
        self._goal_for_next_session_frame = ttk.Labelframe(master=self._frame,
                                                           text='Goal for next session',
                                                           labelanchor='nw',
                                                           padding=5)
        self._goal_for_next_session_entry = ttk.Entry(
            master=self._goal_for_next_session_frame)

    def _define_previously_set_goal_frame(self):
        self._previously_set_goal_frame = ttk.Labelframe(master=self._frame,
                                                         text='Previously set goal',
                                                         labelanchor='nw',
                                                         padding=5)

        self._previously_set_goal_label = ttk.Label(master=self._previously_set_goal_frame,
                                                    text=f'{log_entry_service.get_last_entry_goal()}',
                                                    wraplength=150,
                                                    justify='center')

    def _define_was_last_goal_achieved_frame(self):
        self._was_previous_goal_achieved_frame = ttk.Labelframe(master=self._frame,
                                                                text='Was previously set goal achieved?',
                                                                labelanchor='nw',
                                                                padding=5)

        self._was_last_goal_achieved = StringVar(
            master=self._was_previous_goal_achieved_frame)

        values = (('yes', True), ('no', False))

        # the radio buttons are built here as an exception
        i = 1
        for value in values:
            rad_but = ttk.Radiobutton(
                master=self._was_previous_goal_achieved_frame, text=value[0], value=value[1], variable=self._was_last_goal_achieved)
            rad_but.grid(row=4, column=i, padx=5, pady=5)
            i += 1

    def _define_buttons(self):
        self._go_back_button = ttk.Button(
            master=self._frame,
            text='Back',
            command=self._handle_go_back
        )

        self._save_entry_button = ttk.Button(
            master=self._frame,
            text='Save entry',
            command=self._handle_create_new_log_entry
        )

    def _build_buttons(self):
        self._go_back_button.grid(row=6, column=0, padx=5)

        self._save_entry_button.grid(row=6, column=1, padx=5)

    def _build_was_last_goal_achieved_frame(self):
        self._was_previous_goal_achieved_frame.grid(
            row=4, column=1, padx=5, pady=5)
        # radio buttons are built and defined together
        # in the define function

    def _build_previously_set_goal_frame(self):
        self._previously_set_goal_frame.grid(row=4, column=0, padx=5, pady=5)
        self._previously_set_goal_label.grid()

    def _build_goal_for_next_session_frame(self):
        self._goal_for_next_session_frame.grid(row=5, column=0, padx=5, pady=5)
        self._goal_for_next_session_entry.grid()

    def _build_what_did_not_go_well_frame(self):
        self._what_did_not_go_well_frame.grid(row=3, column=1, padx=5, pady=5)
        self._what_did_not_go_well_entry.grid()

    def _build_what_went_well_frame(self):
        self._what_went_well_frame.grid(row=3, column=0, padx=5, pady=5)
        self._what_went_well_entry.grid()

    def _build_session_style_frame(self):
        self._session_style_frame.grid(row=2, column=0, padx=5, pady=5)
        self.opt_session.grid()

    def _build_date_frame(self):
        self._date_frame.grid(row=1, column=0, padx=5, pady=5)
        self._date_entry.grid()

    def _build_duration_frame(self):
        self._duration_frame.grid(row=1, column=1, padx=5, pady=5)
        self._duration_entry.grid()

    def _define_frames(self):
        self._define_date_frame()
        self._define_duration_frame()
        self._define_session_style_frame()
        self._define_what_went_well_frame()
        self._define_what_did_not_go_well()
        self._define_goal_for_next_session_frame()
        self._define_previously_set_goal_frame()
        self._define_was_last_goal_achieved_frame()
        self._define_buttons()

    def _build_frames(self):
        self._build_date_frame()
        self._build_duration_frame()
        self._build_session_style_frame()
        self._build_what_went_well_frame()
        self._build_what_did_not_go_well_frame()
        self._build_goal_for_next_session_frame()
        self._build_previously_set_goal_frame()
        self._build_was_last_goal_achieved_frame()
        self._build_buttons()

    def _initialize(self):
        self._frame = ttk.LabelFrame(master=self._root, text='Create a log entry',
                                     border=0,
                                     labelanchor='n',
                                     padding=10)

        self._define_frames()

        self._build_frames()
