import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        # create main menu
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

        # create main frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        # create labels
        self.label1 = tk.Label(self.main_frame, text="Expense Name:")
        self.label1.pack()

        self.label2 = tk.Label(self.main_frame, text="Expense Amount:")
        self.label2.pack()

        self.label3 = tk.Label(self.main_frame, text="Expense List:")
        self.label3.pack()

        # create entry boxes
        self.entry1 = tk.Entry(self.main_frame)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.main_frame)
        self.entry2.pack()

        # create buttons
        self.button1 = tk.Button(self.main_frame, text="Add Expense", command=self.add_expense)
        self.button1.pack()

        self.button2 = tk.Button(self.main_frame, text="Clear List", command=self.clear_list)
        self.button2.pack()

        self.button3 = tk.Button(self.main_frame, text="Exit", command=self.on_exit)
        self.button3.pack()

        # create expense listbox
        self.listbox = tk.Listbox(self.main_frame)
        self.listbox.pack()

    def add_expense(self):
        # input validation
        expense_name = self.entry1.get()
        expense_amount = self.entry2.get()
        if not expense_name:
            messagebox.showerror("Error", "Please enter an expense name.")
            return
        if not expense_amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid expense amount.")
            return

        # add expense to listbox
        self.listbox.insert(tk.END, f"{expense_name}: ${expense_amount}")

        # clear entry boxes
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)

    def clear_list(self):
        # clear expense listbox
        self.listbox.delete(0, tk.END)

    def on_exit(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()
