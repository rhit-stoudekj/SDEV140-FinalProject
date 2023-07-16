from tkinter import *
import sqlite3 as sq
import datetime

window = Tk()
window.title("Compound Tracker")

window.geometry('800x600+0+0')

header = Label(window, text="Compound Tracker for Weightlifting", font=("arial”,30,”bold"), fg="black").pack()

window.mainloop()
L1 = Label(window, text = "Compound Lift", font=("arial", 18)).Place(x=10,y=100)

L2 = Label(window, text = "Day (dd)", font=("arial",18)).Place(x=10,y=150)

L3 = Label(window, text = "Month (mm)", font=("arial",18)).Place(x=10,y=200)

L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).Place(x=10,y=250)
L5 = Label(window, text = "Max Weight (KG)", font=("arial",18)).Place(x=10,y=300)
L6 = Label(window, text = "Reps", font=("arial",18)).Place(x=10,y=350)