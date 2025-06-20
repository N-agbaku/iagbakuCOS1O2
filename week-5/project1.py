import tkinter as tk

from docutils.nodes import label


def button_click():
    print("Button clicked!")

    msgbox.showinfo("Info", "Welcome to COS102 GUI APP!\n")

    result = msgbox.askyesno("Configuration", "Do you want to continue?")

root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

label = tk.label(root, text="Hello Friend \n")
label.pack()

button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

button.config(fg='red', bg='yellow')

root.mainloop()
