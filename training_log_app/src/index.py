from tkinter import Tk
from ui.ui import UI

# main loop for program

def main():
    window = Tk()
    window.title('MMA Log Book')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()


    