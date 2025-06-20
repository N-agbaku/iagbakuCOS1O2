import tkinter as tk
from tkinter import messagebox as msgbox  # Correct import

def button_click():
    print("Button clicked!")
    msgbox.showinfo("Info", "Welcome to COS102 GUI APP!\n")
    result = msgbox.askyesno("Configuration", "Do you want to continue?")

root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

label = tk.Label(root, text="Hello Friend \n")  # Capital L
label.pack()

button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

button.config(fg='red', bg='yellow')

root.mainloop()
