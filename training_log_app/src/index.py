from tkinter import Tk
from ui.ui import UI


def main():
    '''Main window for application.
    This function is called with poetry command.
    '''

    window = Tk()
    window.title('MMA Log Book')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
