import tkinter as tk
from tkinter import font

def handlekeypress(event):
    print(event.char)

def button1pressed():
    global display
    if display == "0":
        display = "1"
    else:
        display += "1"

# Window Creation
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = "0"

calc_display = tk.StringVar(window, "", display)

# Button Organization
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

# 1
btn_1 = tk.Button(master=window, text="1", font=(None, 10), command=button1pressed)
btn_1.grid(row=3, column=0, sticky="nsew")
btn_1.bind("<Button-1>", handlekeypress)

# 2
btn_2 = tk.Button(master=window, text="2", font=(None, 10))
btn_2.grid(row=3, column=1, sticky="nsew")

# 3
btn_3 = tk.Button(master=window, text="3", font=(None, 10))
btn_3.grid(row=3, column=2, sticky="nsew")

# 4
btn_4 = tk.Button(master=window, text="4", font=(None, 10))
btn_4.grid(row=2, column=0, sticky="nsew")

# 5
btn_5 = tk.Button(master=window, text="5", font=(None, 10))
btn_5.grid(row=2, column=1, sticky="nsew")

# 6
btn_6 = tk.Button(master=window, text="6", font=(None, 10))
btn_6.grid(row=2, column=2, sticky="nsew")

# 7
btn_7 = tk.Button(master=window, text="7", font=(None, 10))
btn_7.grid(row=1, column=0, sticky="nsew")

# 8
btn_8 = tk.Button(master=window, text="8", font=(None, 10))
btn_8.grid(row=1, column=1, sticky="nsew")

# 9
btn_9 = tk.Button(master=window, text="9", font=(None, 10))
btn_9.grid(row=1, column=2, sticky="nsew")

# 0
btn_0 = tk.Button(master=window, text="0", font=(None, 10))
btn_0.grid(row=4, column=1, sticky="nsew")

# Negative or Positive
btn_negpos = tk.Button(master=window, text="+/-", font=(None, 10))
btn_negpos.grid(row=4, column=0, sticky="nsew")

# Decimal
btn_dot = tk.Button(master=window, text=u"\u2022", font=(None, 10))
btn_dot.grid(row=4, column=2, sticky="nsew")

# Add
btn_plus = tk.Button(master=window, text="+", font=(None, 12))
btn_plus.grid(row=1, column=3, sticky="nsew")

# Subtract
btn_minus = tk.Button(master=window, text="-", font=(None, 15))
btn_minus.grid(row=2, column=3, sticky="nsew")

# Divide
btn_divide = tk.Button(master=window, text="/", font=(None, 12))
btn_divide.grid(row=3, column=3, sticky="nsew")

# Multiplication
btn_multi = tk.Button(master=window, text="x", font=(None, 12))
btn_multi.grid(row=4, column=3, sticky="nsew")

# Label
lbl_value = tk.Label(master=window, text=calc_display, font=(None, 15))
lbl_value.grid(row=0, column=0, columnspan=4, sticky="nse", ipadx=20)

# Equals
btn_equals = tk.Button(master=window, text="=", font=(None, 10))
btn_equals.grid(row=5, column=0, columnspan=2, sticky="nswe")

# Clear
btn_clear = tk.Button(master=window, text="Clear", font=(None, 10))
btn_clear.grid(row=5, column=3, sticky="nswe")

# Backspace
btn_bksp = tk.Button(master=window, text=u"\u232B", font=(None, 10))
btn_bksp.grid(row=5, column=2, sticky="nswe")


def main():
    global calc_display
    window.mainloop()

if __name__ == "__main__":
    main()