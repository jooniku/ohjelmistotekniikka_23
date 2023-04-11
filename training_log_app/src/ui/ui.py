from ui.new_log_entry_view import NewLogEntryView

class UI:
    '''Class responsible for user interface'''

    def __init__(self, root):
        '''
        Arguments:
            root:
                Tkinter element to create the ui in'''
        
        self._root = root
        self._current_view = None
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def start(self):
        '''Start ui, CURRENTLY starts at add log entry view, not login page'''
        self._show_new_log_entry_view()

    
    def _show_new_log_entry_view(self):
        self._hide_current_view()

        self._current_view = NewLogEntryView(self._root)

        self._current_view.pack()