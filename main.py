import tkinter as tk
from tkinter import ttk
from tkinter import *
window = tk.Tk() 
#this is for title
window.title("Fees recipet form")
frame = tkinter.Frame(window)
frame.pack(padx = 30,pady = 40)
#this is for name
first = tkinter.Label(frame, text = "NAME")
first.grid(row = 0,column = 0)
name_entry = tkinter.Entry(frame, text='FULL Name') 
name_entry.grid(row=0,column = 1)
#This is for gender
first1 = tkinter.Label(frame, text = "GENDER")
first1.grid(row = 1,column = 0)
v = IntVar()
Radiobutton(frame, text='MALE', variable=v, value=1).grid(row=1,column = 1, sticky=W)
Radiobutton(frame, text='FEMALE', variable=v, value=2).grid(row=1,column =2, sticky=W)

#THIS IS FOR APPLICATION NUMBER :
application = tkinter.Label(frame, text = "APPLICATION NUMBER")
application.grid(row = 4,column = 0)
application_entry = tkinter.Entry(frame, text='application number') 
application_entry.grid(row=4,column = 1)
#this is for course name:

course = tkinter.Label(frame, text = "COURSE NAME")
course.grid(row = 5,column = 0)

def on_select(event):
     selected_item = combo_box.get()
     label.config(text="COURSE NAMES " + selected_item)

# root = tk.Tk()
# root.title("COURSES NAMES")

# Create a label
# label = tk.Label(frame, text="COURSE NAMES")
# label.grid(row = 5,column = 1)

# Create a Combobox widget
combo_box = ttk.Combobox(frame, values=["DATA SCIENCE", "DATA ANALYSIS", "PYTHON","MACHINE LEARNING"])
combo_box.grid(row = 5,column = 1)

# Set default value
combo_box.set("DATA SCIENCE")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)

#THIS IS FOR PAYMENT MODE

payment = tkinter.Label(frame, text = "PAYMENT MODE:")
payment.grid(row = 7,column = 0)
p = IntVar()
Radiobutton(frame, text='CASH', variable=p, value=1).grid(row=7,column = 1, sticky=W)
Radiobutton(frame, text='UPI', variable=p, value=2).grid(row=7,column =2, sticky=W)

#THIS IS FOR FEES AMOUNT
fees = tkinter.Label(frame, text = "Enter fees amount")
fees.grid(row = 8,column = 0)
application_entry = tkinter.Entry(frame, text='application number') 
application_entry.grid(row=8,column = 1)

#this is for the submit button
submit= tkinter.Button(frame, text = "SUBMIT")
submit.grid(row = 9,column = 1)

window.mainloop()
