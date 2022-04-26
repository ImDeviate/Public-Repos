import tkinter as tk
from datetime import datetime, time

window = tk.Tk()
label = tk.Label(window)
window.configure(bg="magenta")
window.rowconfigure([0, 1], weight=1)
window.columnconfigure([0], weight=1)

#---------------------------

def countdown():
    futuredate = datetime.strptime('Sep 12 2021  00:00', '%b %d %Y %H:%M')

    nowdate = datetime.now()
    count = int((futuredate-nowdate).total_seconds())

    days = count//86400
    hours = (count-days*86400)//3600
    minutes = (count-days*86400-hours*3600)//60
    seconds = count-days*86400-hours*3600-minutes*60
    poggers="{} days {} hours {} minutes {} seconds".format(days, hours, minutes, seconds)
    return poggers

#---------------------------

def drawlabel():
    label["font"] = ("Arial", 20)
    label["fg"] = "white"
    label["bg"] = "magenta"
    label["text"] = countdown()
    label.grid(row=1, column=0, sticky="nsew")
    window.after(1000,drawlabel)

#---------------------------

title = tk.Label(
    text="Time Until Birthday:",
    fg="white",
    bg="magenta",
    font=("Arial",20)
)
title.grid(row=0, column=0)

#---------------------------

def main():
    window.title("Days until my Birthday")
    window.geometry("550x100")
    drawlabel()
    window.mainloop()

if __name__ == "__main__":
    main()