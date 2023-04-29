import tkinter as tk
from tkinter import messagebox

from expense_tracker_gui import ExpenseTrackerGUI
from expense_tracker_data import ExpenseTrackerData

if __name__ == '__main__':
    # create data object
    data = ExpenseTrackerData()

    # create root window and GUI object
    root = tk.Tk()
    app = ExpenseTrackerGUI(root, data)

    # load saved data
    try:
        data.load_data()
    except FileNotFoundError:
        pass

    # start GUI loop
    root.mainloop()

    # save data on exit
    data.save_data()
