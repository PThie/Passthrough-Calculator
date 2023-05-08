# --------------------------------------------------
# import modules
import tkinter as tk
from tkinter import ttk

#--------------------------------------------------
# overall settings

window = tk.Tk()
window.title("Pass-through and Price reduction")
window.resizable(True, True)
window.geometry("500x250")
window.tk.call("tk", "scaling", 2.0)

input_frame = ttk.Frame(master = window, width = 100, height = 50)
input_frame.pack()

#--------------------------------------------------
# globals

mean_price_diesel = 1.97716
mean_price_e10 = 1.80839

discount_diesel = 16.71
discount_e10 = 35.16

#--------------------------------------------------
# function for capturing price effect input

def get_price_input():
    try:
        # convert entered price into number (if possible)
        user_price = float(price_entry.get())
        # if it worked, keep warning empty
        nonumber["text"] = ""
        
        if fueltype.get() == "nothing":
            nonumber["text"] = "Please select a fuel type!"
        if fueltype.get() == "diesel":
            pass_through["text"] = round((user_price / discount_diesel) * 100, 3)
            reduction["text"] = round(user_price / mean_price_diesel, 3)
        if fueltype.get() == "e10":
            pass_through["text"] = round((user_price / discount_e10) * 100, 3)
            reduction["text"] = round(user_price / mean_price_e10, 3)

    except ValueError:
        nonumber["text"] = "Please enter a valid number!"
    
#--------------------------------------------------
# function for resetting

def reset():
    fueltype.set("0")
    price_entry.delete(0, tk.END)
    pass_through["text"] = "0"
    reduction["text"] = "0"
    nonumber["text"] = ""

#--------------------------------------------------
# price effect entry

price_label = ttk.Label(
    master = input_frame,
    text = "Enter price effect (in Cents):"
)

price_entry = ttk.Entry(
    master = input_frame,
    width = 20
)

price_label.grid(column = 0, row = 0, sticky = tk.W)
price_entry.grid(column = 1, row = 0, sticky = tk.W)

#--------------------------------------------------
# make sure that the entry is a number
# otherwise print error

nonumber = tk.Label(
    master = input_frame,
    text = "",
    fg = "red"
)

nonumber.grid(column = 0, row = 6, pady = 20, sticky = tk.W)

#--------------------------------------------------
# check box for diesel

fueltype = tk.StringVar(value = "nothing")
diesel_check = ttk.Radiobutton(
    master = input_frame,
    text = "Diesel",
    variable = fueltype,
    value = "diesel",
    command = lambda: fueltype.get()
)

diesel_check.grid(column = 0, row = 2, sticky = tk.W, pady = 5)

#--------------------------------------------------
# check box for e10

# e10 = tk.StringVar()
e10_check = ttk.Radiobutton(
    master = input_frame,
    text = "E10",
    variable = fueltype,
    value = "e10",
    command = lambda: fueltype.get() 
)

e10_check.grid(column = 1, row = 2, sticky= tk.W, pady = 5)

#--------------------------------------------------
# button for submitting entry

okay_button = ttk.Button(
    master = input_frame,
    text = "Submit",
    command = get_price_input
)

okay_button.grid(column = 0, row = 3, pady = 5)

#--------------------------------------------------
# button for reset

reset_button = ttk.Button(
    master = input_frame,
    text = "Reset",
    command = reset
)

reset_button.grid(column = 1, row = 3, pady = 5)

#--------------------------------------------------
# output the pass-through rate

pass_through_label = ttk.Label(
    master = input_frame,
    text = "Pass-through rate (%):"
)

pass_through = ttk.Label(
    master = input_frame,
    text = "0"
)
pass_through_label.grid(column = 0, row = 4, pady = 5, sticky = tk.W)
pass_through.grid(column = 1, row = 4, pady = 5, sticky = tk.W, padx = 10)

#--------------------------------------------------
# output mean price reduction

reduction_label = ttk.Label(
    master = input_frame,
    text = "Price reduction in means (%):"
)

reduction = ttk.Label(
    master = input_frame,
    text = "0"
)

reduction_label.grid(column = 0, row = 5, pady = 5, sticky = tk.W)
reduction.grid(column = 1, row = 5, pady = 5, sticky = tk.W, padx = 10)

#--------------------------------------------------
# start application

window.mainloop()