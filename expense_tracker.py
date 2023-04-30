# Expense Tracker GUI Application
# Author: [Ethan Chadwick]
# Date: [4/30/2023]
# Description: This program is a simple GUI application that allows users to track their expenses. It has two windows, modular approach, three labels, three buttons, at least three callback functions with each button, including an exit button. The program uses secure coding best practices, including input validation, to ensure that the user enters the correct data type and that the entry box is not empty. Each module has a header comment explaining its purpose, and variables are commented at their declaration.

import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.geometry("300x200")

        # Create a label for amount
        self.amount_label = tk.Label(self.master, text="Amount:")
        self.amount_label.pack()

        # Create an entry box for amount
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        # Create a label for description
        self.description_label = tk.Label(self.master, text="Description:")
        self.description_label.pack()

        # Create an entry box for description
        self.description_entry = tk.Entry(self.master)
        self.description_entry.pack()

        # Create a label for category
        self.category_label = tk.Label(self.master, text="Category:")
        self.category_label.pack()

        # Create an entry box for category
        self.category_entry = tk.Entry(self.master)
        self.category_entry.pack()

        # Create a button to add an expense
        self.add_button = tk.Button(self.master, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        # Create a button to view all expenses
        self.view_button = tk.Button(self.master, text="View Expenses", command=self.view_expenses)
        self.view_button.pack()

        # Create a button to exit the application
        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)
        self.exit_button.pack()
    
        # Create a label with an image and alternate text
        photo = tk.PhotoImage(file="final/images.jpg")
        label = tk.Label(root, image=photo, text="Picture of an Expense Tracker", compound="top")
        label.pack()

        # Create a label with an image and alternate text
        photo = tk.PhotoImage(file="final/images2.png")
        label = tk.Label(root, image=photo, text="Picture of an Expense Tracker", compound="top")
        label.pack()
    
    def add_expense(self):
        """Add an expense to the list"""
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()

        # Check if the amount is a valid number
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        # Check if the description and category are not empty
        if not description:
            messagebox.showerror("Error", "Please enter a description")
            return
        if not category:
            messagebox.showerror("Error", "Please enter a category")
            return

        # Add the expense to the list
        expense = {"amount": amount, "description": description, "category": category}
        expenses.append(expense)

        # Clear the entry boxes
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Expense added successfully")

    def view_expenses(self):
        """View all expenses in a new window"""
        expenses_window = tk.Toplevel(self.master)
        expenses_window.title("Expenses")
        expenses_window.geometry("300x200")

        # Create a label to display all expenses
        expenses_text = "\n".join([f"{expense['amount']}: {expense['description']} ({expense['category']})" for expense in expenses])
        expenses_label = tk.Label(expenses_window, text=expenses_text)
        expenses_label.pack()

    def exit_application(self):
        """Exit the application"""
        self.master.destroy()

if __name__ == "__main__":
    expenses = []
    root = tk.Tk()
    expense_tracker = ExpenseTracker(root)
    root.mainloop()
    # End of Program
