from tkinter import ttk


class NightMode:
    '''Class to show user interface in night mode theme.
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
        self.app_style.configure('background.TFrame', background='#2C3E50')
        self.app_style.configure(
            'text.TLabel', background='#2C3E50', foreground='#ECF0F1')

    def config_buttons(self):
        self.app_style.configure(
            'button.TButton', background='#23313f', foreground='#ECF0F1', relief='flat')
        self.app_style.map('button.TButton', relief=[
            ('active', 'ridge')], background=[('active', '#31404f')])
        self.app_style.configure(
            'login_button.TButton', background='#2C3E50', foreground='#ECF0F1', relief='groove')
        self.app_style.map('login_button.TButton',  relief=[
            ('active', 'ridge')], background=[('active', '#31404f')])

    def config_navbar(self):
        self.app_style.configure(
            'navbar.TFrame', background='#23313f', relief='flat')
        self.app_style.configure('navbar_text.TLabel',
                                 background='#23313f', foreground='#ECF0F1')

    def config_inner_frames(self):
        self.app_style.configure('inner_frame.TFrame',
                                 background='#31404f', relief='sunken')
        self.app_style.configure('inside_text.TLabel',
                                 background='#31404f', foreground='#ECF0F1')
        self.app_style.configure('input_field.TEntry', background='#ECF0F1')

        self.inner_colour = '#31404f'
        self.inner_text_colour = '#ECF0F1'
        self.graph_bar_colour = '#3498DB'

    def config_login_styles(self):
        self.app_style.configure('login_frame.TFrame',
                                 background='#31404f', relief='sunken')
        self.app_style.configure('login_text.TLabel',
                                 background='#31404f', foreground='#ECF0F1')

    def config_radio_button_style(self):
        self.app_style.configure('radio_button.TRadiobutton',
                                 background='#31404f', foreground='#ECF0F1')
        self.app_style.map('radio_button.TRadiobutton',
                           background=[('active', '#31404f')])

    def config_option_menu_style(self):
        self.app_style.configure('menu.TMenubutton',
                                 background='#2C3E50', foreground='#ECF0F1')
        self.app_style.map('menu.TMenubutton',  relief=[
            ('active', 'ridge')], background=[('active', '#31404f')])

    def config_calendar_style(self):
        self.calendar_color = '#2980B9'
