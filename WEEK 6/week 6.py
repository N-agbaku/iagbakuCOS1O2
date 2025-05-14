
import tkinter as tk
from tkinter import messagebox

def calculate_fee():
    try:
        weight = float(weight_entry.get())
        location = location_var.get()

        if location == "Ibeju-Lekki":
            if weight >= 10:
                fee = 5000
            else:
                fee = 3500
        elif location == "Epe":
            if weight >= 10:
                fee = 10000
            else:
                fee = 5000
        else:
            messagebox.showerror("Error", "Please select a valid location.")
            return

        result_label.config(text=f"Delivery Fee: ₦{fee}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid weight.")

# GUI setup
root = tk.Tk()
root.title("Simi Services Delivery Fee Calculator")

tk.Label(root, text="Enter Package Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Select Location:").pack()
location_var = tk.StringVar(value="Ibeju-Lekki")
tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe").pack()

tk.Button(root, text="Calculate Fee", command=calculate_fee).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
