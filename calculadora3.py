from tkinter import *
from tkinter import ttk
from math import *

root  = Tk()
root.title("Calculator")
root.geometry("+500+80")

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0)

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1)
label_entrada1.grid(column = 0, row =0)

enrtada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable = enrtada2)

button = ttk.Button(mainframe, text= 0)