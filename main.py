from tkinter import *
from tkinter import ttk

def addchar(symbol):
    res.set(res.get() + str(symbol))
    return

def calculate(*args):
    try:
        val = eval(res.get())
        res.set(val)
    except ValueError:
        res.set("Value Error")
        clear()
        pass
    except ZeroDivisionError:
        res.set("Can't divide by 0")
        clear()
        pass
    except SyntaxError:
        pass
def clear(*args):
    try:
        res.set(" ")
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
ttk.Button(mainframe, text = "1",command=lambda:addchar('1')).grid(column=0,row=1)
ttk.Button(mainframe, text = "2",command=lambda:addchar('2')).grid(column=1,row=1)
ttk.Button(mainframe, text = "3",command=lambda:addchar('3')).grid(column=2,row=1)
ttk.Button(mainframe, text = "4",command=lambda:addchar('4')).grid(column=0,row=2)
ttk.Button(mainframe, text = "5",command=lambda:addchar('5')).grid(column=1,row=2)
ttk.Button(mainframe, text = "6",command=lambda:addchar('6')).grid(column=2,row=2)
ttk.Button(mainframe, text = "7",command=lambda:addchar('7')).grid(column=0,row=3)
ttk.Button(mainframe, text = "8",command=lambda:addchar('8')).grid(column=1,row=3)
ttk.Button(mainframe, text = "9",command=lambda:addchar('9')).grid(column=2,row=3)
ttk.Button(mainframe, text = "0",command=lambda:addchar('0')).grid(column=1,row=4)
ttk.Button(mainframe, text = "+",command=lambda:addchar('+')).grid(column=3,row=1)
ttk.Button(mainframe, text = "-",command=lambda:addchar('-')).grid(column=3,row=2)
ttk.Button(mainframe, text = "/",command=lambda:addchar('/')).grid(column=3,row=3)
ttk.Button(mainframe, text = "*",command=lambda:addchar('*')).grid(column=3,row=4)
ttk.Button(mainframe, text = "=",command=calculate).grid(column=2,row=4)
ttk.Button(mainframe,text="C", command=clear).grid(column=0,row=4)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

root.bind("<Return>",calculate)
root.mainloop()