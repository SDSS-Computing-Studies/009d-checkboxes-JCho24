#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
state1 = IntVar()
state1.set(0)
state2 = IntVar()
state2.set(0)
state3 = IntVar()
state3.set(0)
state4 = IntVar()
state4.set(0)
state5 = IntVar()
state5.set(0)
state6 = IntVar()
state6.set(0)
state7 = IntVar()
state7.set(0)
state8 = IntVar()
state8.set(0)




def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    decimal = 0
    for i in range(0,8):
        if binary[i] == 1:
           decimal = decimal + (128 / (2**i))
        elif binary[i] == 0:
            pass

    return decimal 
    

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's

    return binary
    

def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    binary = decimal_to_binary(decimal)

    


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []

    binary.append(state1.get())
    binary.append(state2.get())
    binary.append(state3.get())
    binary.append(state4.get())
    binary.append(state5.get())
    binary.append(state6.get())
    binary.append(state7.get())
    binary.append(state8.get())


    decimal = binary_to_decimal(binary)
    e1.delete(0,END)
    e1.insert(0, decimal)
    

title = Label(win, text = "Binary / Decimal Converter!")

cb1 = Checkbutton(win, variable = state1)
cb2 = Checkbutton(win, variable = state2)
cb4 = Checkbutton(win, variable = state3)
cb8 = Checkbutton(win, variable = state4)
cb16 = Checkbutton(win, variable = state5)
cb32 = Checkbutton(win, variable = state6)
cb64 = Checkbutton(win, variable = state7)
cb128 = Checkbutton(win, variable = state8)

b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)

e1 = Entry(win)


title.grid(row = 1, column = 1, columnspan = 8)

cb1.grid(row = 2, column = 1)
cb2.grid(row = 2, column = 2)
cb4.grid(row = 2, column = 3)
cb8.grid(row = 2, column = 4)
cb16.grid(row = 2, column = 5)
cb32.grid(row = 2, column = 6)
cb64.grid(row = 2, column = 7)
cb128.grid(row = 2, column = 8)

b1.grid(row = 3, column = 1, columnspan = 4)
b2.grid(row = 3, column = 5, columnspan = 4)

e1.grid(row = 4, column = 1, columnspan = 8)



win.mainloop()