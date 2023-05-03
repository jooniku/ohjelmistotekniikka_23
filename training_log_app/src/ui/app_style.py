from ui.themes.daymode import DayMode
from ui.themes.nightmode import NightMode

from tkinter import ttk


class AppStyle:
    '''Class responsible for styling the user interface.
    Has parameter current_style which holds the style class
    itself.
    '''

    def __init__(self, theme):
        '''Initialize style.

        Args:
            theme (str): theme name, which is class name like DayMode
        '''

        # turn theme string into class object
        self.current_style = globals()[theme]()

        self.set_font()

    def set_font(self):
        ttk.Style().configure('.', font=('Khmer OS', 11))

    def get_calendar_colour(self):
        '''Returns the calendar widget
        color for current style
        '''

        return self.current_style.calendar_color

    def get_graph_bar_colour(self):
        '''Returns the colour of graphs bars
        made with matplotlib, so it can't use
        tkinter styles
        '''

        return self.current_style.graph_bar_colour

    def get_inner_frame_colour(self):
        '''Returns the colour of inner frame
        background. Mainly used for other package
        styling than tkinter widgets.
        '''

        return self.current_style.inner_colour

    def get_inner_frame_text_colour(self):
        '''Returns the colour of inner frames text.
        Useful for packages other than tkinter.
        '''

        return self.current_style.inner_text_colour

    def change_style(self):
        '''Switches ui style from 
        day -> night or night -> day
        '''
        if type(self.current_style) == NightMode:
            self.current_style = DayMode()
        else:
            self.current_style = NightMode()
