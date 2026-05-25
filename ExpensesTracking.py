import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = "expenses.csv"


if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["date", "category", "amount", "description"])
    df.to_csv(FILE, index=False)


def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    desc = desc_entry.get()

    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "Please fill required fields")
        return

    df = pd.read_csv(FILE)

    new_row = pd.DataFrame([[date, category, float(amount), desc]],
                           columns=df.columns)

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE, index=False)

    messagebox.showinfo("Success", "Expense Added!")

    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)


def show_summary():
    df = pd.read_csv(FILE)

    total = df["amount"].sum()
    by_cat = df.groupby("category")["amount"].sum()

    message = f"Total Expenses: {total}\n\nBy Category:\n{by_cat}"
    messagebox.showinfo("Summary", message)


def show_chart():
    df = pd.read_csv(FILE)

    df.groupby("category")["amount"].sum().plot(kind="bar")
    plt.title("Expenses by Category")
    plt.show()



root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

tk.Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Description").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="Show Summary", command=show_summary).pack(pady=5)
tk.Button(root, text="Show Chart", command=show_chart).pack(pady=5)

root.mainloop()