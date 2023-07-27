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

# Create variables for each list
comp = StringVar(window)
comp.set('----')  #placeholder

compdb = StringVar(window)  #second dropdown list
compdb.set('----')

day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
weight = StringVar(window)
reps = StringVar(window)

# Options for drop down list
compound = {'Bench', 'Squat', 'Deadlift', 'RDL'}

compM = OptionMenu(window, comp, *compound)  # For 1st drop down list
compM.place(x=220, y=105)

compbase = OptionMenu(window, compdb, *compound)  # For 2nd drop down list
compbase.place(x=100, y=500)

# Entry for 'input' in GUI
day = Entry(window, textvariable=day)
day.place(x=220, y=155)

month = Entry(window, textvariable=month)
month.place(x=220, y=205)

year = Entry(window, textvariable=year)
year.place(x=220, y=255)

weight = Entry(window, textvariable=weight)
weight.place(x=220, y=305)

rep = Entry(window, textvariable=reps)
rep.place(x=220, y=355)


# submit to database
def submit():
    print("You have submitted a record")

    c.execute(
        'CREATE TABLE IF NOT EXISTS ' + comp.get() + ' (Datestamp TEXT, MaxWeight INTEGER, Reps INTEGER)')

    date = datetime.date(int(year.get()), int(month.get()), int(day.get()))  # Date

    c.execute('INSERT INTO ' + comp.get() + ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',
              (date, weight.get(), reps.get()))  # Insert record into database.
    con.commit()

    # Reset fields after submit
    comp.set('----')
    day.set('')
    month.set('')
    year.set('')
    weight.set('')
    reps.set('')


# Clear boxes when submit button is hit
def remove():
    comp.set('----')
    compdb.set('----')
    day.set('')
    month.set('')
    year.set('')
    weight.set('')
    reps.set('')


def store():
    c.execute('SELECT * FROM ' + compdb.get())  # Select from which ever compound lift is selected

    frame = Frame(window)
    frame.place(x=400, y=150)

    Listb = Listbox(frame, height=8, width=25, font=("arial", 12))
    Listb.pack(side=LEFT, fill=Y)

    scroll = Scrollbar(frame, orient=VERTICAL)  # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command=Listb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Listb.config(yscrollcommand=scroll.set)

    Listb.insert(0, 'Date, Max Weight, Reps')  # first row in listbox

    data = c.fetchall()  # Gets the data from the table

    for row in data:
        Listb.insert(1, row)  # Inserts record row by row in list box

    L7 = Label(window, text=compdb.get() + '      ',
               font=("arial", 16)).place(x=400, y=100)  # Title of list box, given which compound lift is chosen

    L8 = Label(window, text="Ordered from Newest to Oldest",
               font=("arial", 16)).place(x=400, y=350)
    con.commit()


submitb = Button(window, text="Submit", command=submit)
submitb.place(x=100, y=400)

clearb = Button(window, text="Clear", command=remove)
clearb.place(x=10, y=400)

storeb = Button(window, text="Open History", command=store)
storeb.place(x=10, y=500)

window.mainloop()  # mainloop() -> make sure that window stays open
