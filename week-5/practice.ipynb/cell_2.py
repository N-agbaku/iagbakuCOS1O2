import tkinter as tk
from tkinter import messagebox

from Demos.win32ts_logoff_disconnected import username
from PIL import Image, ImageTk
from PyQt5.QtSql import password


def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.label(window, text=f("Welcome {username}\n")
    label_1.pack()
    label_2 = tk.label(window, text="This is python GUI with Tkinter")
    label_2.pack()

    root.mainloop()

def submit():
    username = username_entry.get()
    password =  password_entry.get()

    if username = "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login","Invalid username or password")

root = tk.Tk()
root.title("Login Form")
root.geometry