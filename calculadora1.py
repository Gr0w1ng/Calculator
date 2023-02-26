from tkinter import *

window = Tk()
window.title("Calculadora")

i = 0

#ENTRADA

e_text=Entry(window, font="calibri 20")
e_text.grid(row=0, column=0, columnspan=4, padx= 5, pady=5)

#FUNCIONES
def click_botton(valor):
    global i
    e_text.insert(i, valor) 
    i+=1
    
def erase():
    e_text.delete(0, END)
    i = 0
    
def resolve():
    operation = e_text.get()
    result = eval(operation)
    e_text.delete(0, END)
    e_text.insert(0, result)     
    i = 0
    
#BOTONES
boton1 = Button(window, text="1", width=5, height=2, command= lambda: click_botton(1))
boton2 = Button(window, text="2", width=5, height=2, command= lambda: click_botton(2))
boton3 = Button(window, text="3", width=5, height=2, command= lambda: click_botton(3))
boton4 = Button(window, text="4", width=5, height=2, command= lambda: click_botton(4))
boton5 = Button(window, text="5", width=5, height=2, command= lambda: click_botton(5))
boton6 = Button(window, text="6", width=5, height=2, command= lambda: click_botton(6))
boton7 = Button(window, text="7", width=5, height=2, command= lambda: click_botton(7))
boton8 = Button(window, text="8", width=5, height=2, command= lambda: click_botton(8))
boton9 = Button(window, text="9", width=5, height=2, command= lambda: click_botton(9))
boton0 = Button(window, text="0", width=13, height=2, command= lambda: click_botton(0))

boton_erase = Button(window, text="AC", width=5, height=2, command= lambda: erase())
boton_parentesis1 = Button(window, text="(", width=5, height=2, command= lambda: click_botton("("))
boton_parentesis2= Button(window, text=")", width=5, height=2, command= lambda: click_botton(")"))
boton_punto = Button(window, text=".", width=5, height=2, command= lambda: click_botton("."))

boton_div = Button(window, text="/", width=5, height=2, command= lambda: click_botton("/"))
boton_mult = Button(window, text="x", width=5, height=2, command= lambda: click_botton("*"))
boton_sum = Button(window, text="+", width=5, height=2, command= lambda: click_botton("+"))
boton_rest = Button(window, text="-", width=5, height=2, command= lambda: click_botton("-"))
boton_igual = Button(window, text="=", width=5, height=2, command= lambda: resolve())

#AGREGAR BOTONES

boton_erase.grid(row = 1, column= 0, padx= 5, pady=5)
boton_parentesis1.grid(row = 1, column= 1, padx= 5, pady=5) 
boton_parentesis2.grid(row = 1, column= 2, padx= 5, pady=5) 
boton_div.grid(row = 1, column= 3, padx= 5, pady=5) 

boton7.grid(row = 2, column= 0, padx= 5, pady=5) 
boton8.grid(row = 2, column= 1, padx= 5, pady=5) 
boton9.grid(row = 2, column= 2, padx= 5, pady=5) 
boton_mult.grid(row = 2, column= 3, padx= 5, pady=5)

boton4.grid(row = 3, column= 0, padx= 5, pady=5) 
boton5.grid(row = 3, column= 1, padx= 5, pady=5) 
boton6.grid(row = 3, column= 2, padx= 5, pady=5) 
boton_sum.grid(row = 3, column= 3, padx= 5, pady=5) 

boton1.grid(row = 4, column= 0, padx= 5, pady=5) 
boton2.grid(row = 4, column= 1, padx= 5, pady=5) 
boton3.grid(row = 4, column= 2, padx= 5, pady=5) 
boton_rest.grid(row = 4, column= 3, padx= 5, pady=5) 

boton0.grid(row = 5, column= 0,columnspan=2 , padx= 5, pady=5) 
boton_punto.grid(row = 5, column= 2, padx= 5, pady=5) 
boton_igual.grid(row = 5, column= 3, padx= 5, pady=5) 

window.mainloop()