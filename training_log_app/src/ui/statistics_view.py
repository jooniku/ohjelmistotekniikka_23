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

    def _define_statistics_frame(self):
        # how and what stats should there be
        pass


    def _initialize(self):
        # initialize window
        self._frame = ttk.Frame(master=self._root)
        self.heading_label = ttk.Label(master=self._frame, text='Statistics')

        self._style_config()

        self.padx = 10
        self.pady = 10

        # define variables and get values from database etc.
        self._define_nav_bar_frame()
        self._define_statistics_frame()
        self._define_last_entry_frame()

        # write variables to window aka build the ui
        self._build_nav_bar_frame()
        self._build_statistics_frame()
        self._build_last_entry_frame()
