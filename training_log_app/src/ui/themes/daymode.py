from tkinter import ttk


class DayMode:
    '''Class to show user interface in day mode theme.
    '''

    def __init__(self):
        self.app_style = ttk.Style()

        self.configure_style()

    def configure_style(self):
        self.config_background()
        self.config_buttons()
        self.config_inner_frames()
        self.config_login_styles()
        self.config_navbar()
        self.config_calendar_style()
        self.config_option_menu_style()
        self.config_radio_button_style()

    def config_background(self):
        self.app_style.configure('background.TFrame', background='#FDEFEF')
        self.app_style.configure(
            'text.TLabel', background='#FDEFEF', foreground='#202020')

    def config_buttons(self):
        self.app_style.configure(
            'button.TButton', background='#DAD0C2', foreground='#202020', relief='flat')
        self.app_style.map('button.TButton', relief=[
            ('active', 'ridge')], background=[('active', '#CDBBA7')])
        self.app_style.configure(
            'login_button.TButton', background='#DAD0C2', foreground='#202020', relief='groove')
        self.app_style.map('login_button.TButton',  relief=[
            ('active', 'ridge')], background=[('active', '#CDBBA7')])

    def config_navbar(self):
        self.app_style.configure(
            'navbar.TFrame', background='#DAD0C2', relief='flat')
        self.app_style.configure('navbar_text.TLabel',
                                 background='#DAD0C2', foreground='#202020')

    def config_inner_frames(self):
        self.app_style.configure('inner_frame.TFrame',
                                 background='#F4DFD0', relief='sunken')
        self.app_style.configure('inside_text.TLabel',
                                 background='#F4DFD0', foreground='#202020')
        self.app_style.configure('input_field.TEntry', background='#ECF0F1')

        self.inner_colour = '#F4DFD0'
        self.inner_text_colour = '#202020'
        self.graph_bar_colour = '#505050'

    def config_login_styles(self):
        self.app_style.configure('login_frame.TFrame',
                                 background='#F4DFD0', relief='sunken')
        self.app_style.configure('login_text.TLabel',
                                 background='#F4DFD0', foreground='#202020')

    def config_radio_button_style(self):
        self.app_style.configure('radio_button.TRadiobutton',
                                 background='#F4DFD0', foreground='#202020')
        self.app_style.map('radio_button.TRadiobutton',
                           background=[('active', '#F4DFD0')])

    def config_option_menu_style(self):
        self.app_style.configure('menu.TMenubutton',
                                 background='#F4DFD0', foreground='#202020')
        self.app_style.map('menu.TMenubutton',  relief=[
            ('active', 'ridge')], background=[('active', '#CDBBA7')])

    def config_calendar_style(self):
        self.calendar_color = '#CDBBA7'
