from tkinter import *
from tkinter import ttk

def add1():
    equation.set(equation.get() + "1")
def add2():
    equation.set(equation.get() + "2")
def add3():
    equation.set(equation.get() + "3")
def add4():
    equation.set(equation.get() + "4")
def add5():
    equation.set(equation.get() + "5")
def add6():
    equation.set(equation.get() + "6")
def add7():
    equation.set(equation.get() + "7")
def add8():
    equation.set(equation.get() + "8")
def add9():
    a = equation.get()
    equation.set(a+"9")
def add0():
    equation.set(equation.get() + "0")
def addplus():
    equation.set(equation.get() +"+")
def addminus():
    equation.set(equation.get() +"-")
def adddiv():
    equation.set(equation.get() +"/")
def addmult():
    equation.set(equation.get() +"*")
def calculate(*args):
    try:
        val = eval(equation.get())
        res.set(val)
        clear()
    except ValueError:
        pass
def clear(*args):
    try:
        equation.set(" ")
    except ValueError:
        pass

root = Tk()
root.title("Calculator")
mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
equation = StringVar()
res = StringVar()
ttk.Label(mainframe,textvariable=equation).grid(column=0,row=0)
ttk.Label(mainframe,textvariable=res).grid(column=2,row=0)
ttk.Button(mainframe, text = "1",command=add1).grid(column=0,row=1)
ttk.Button(mainframe, text = "2",command=add2).grid(column=1,row=1)
ttk.Button(mainframe, text = "3",command=add3).grid(column=2,row=1)
ttk.Button(mainframe, text = "4",command=add4).grid(column=0,row=2)
ttk.Button(mainframe, text = "5",command=add5).grid(column=1,row=2)
ttk.Button(mainframe, text = "6",command=add6).grid(column=2,row=2)
ttk.Button(mainframe, text = "7",command=add7).grid(column=0,row=3)
ttk.Button(mainframe, text = "8",command=add8).grid(column=1,row=3)
ttk.Button(mainframe, text = "9",command=add9).grid(column=2,row=3)
ttk.Button(mainframe, text = "0",command=add0).grid(column=1,row=4)
ttk.Button(mainframe, text = "+",command=addplus).grid(column=3,row=1)
ttk.Button(mainframe, text = "-",command=addminus).grid(column=3,row=2)
ttk.Button(mainframe, text = "/",command=adddiv).grid(column=3,row=3)
ttk.Button(mainframe, text = "*",command=addmult).grid(column=3,row=4)
ttk.Button(mainframe, text = "=",command=calculate).grid(column=2,row=4)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

root.bind("<Return>",calculate)
root.mainloop()