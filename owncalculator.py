#Calculadora

from tkinter import *
from tkinter import ttk
from math import *

window = Tk()
window.title("Calculadora")
window.geometry("400x600")
window.resizable(0,0)

# FUNCIONES

def ingresarValores(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)
        
    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
        
        entrada2.set("")
    if tecla == "=":
        entrada1.set(entrada1.get()+entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def borrar(*args):
    inicio = 0   
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def borrarTodo(*args):
    entrada1.set("")
    entrada2.set("")

def raizCuadrada():
    entrada1.set("")
    resultado = sqrt(float(entrada2.get()))    
    entrada2.set(resultado)

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("M.TFrame", background="#DBDBDB")

mainframe = ttk.Frame(window, style="M.TFrame")
mainframe.grid(column = 0, row =0, sticky = (N, E, S ,W))

estilosLabel1 = ttk.Style()
estilosLabel1.configure("label1.TLabel", font= "arial 15", anchor = "e") 

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable= entrada1, style="label1.TLabel")
label_entrada1.grid(column = 0, row =0, columnspan=4,sticky=(N, E, S ,W))

estilosLabel2 = ttk.Style()
estilosLabel2.configure("label2.TLabel", font= "arial 40", anchor = "e") 

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable = entrada2,style="label2.TLabel")
label_entrada2.grid(column = 0, row =1, columnspan=4,sticky=(N, E, S ,W ))

#BOTONES
button0 = ttk.Button(mainframe, text= 0, style="Botones_numeros.TButton", command= lambda: ingresarValores("0"))
button1 = ttk.Button(mainframe, text= 1, style="Botones_numeros.TButton", command= lambda: ingresarValores("1"))
button2 = ttk.Button(mainframe, text= 2, style="Botones_numeros.TButton", command= lambda: ingresarValores("2"))
button3 = ttk.Button(mainframe, text= 3, style="Botones_numeros.TButton", command= lambda: ingresarValores("3"))
button4 = ttk.Button(mainframe, text= 4, style="Botones_numeros.TButton", command= lambda: ingresarValores("4"))
button5 = ttk.Button(mainframe, text= 5, style="Botones_numeros.TButton", command= lambda: ingresarValores("5"))
button6 = ttk.Button(mainframe, text= 6, style="Botones_numeros.TButton", command= lambda: ingresarValores("6"))
button7 = ttk.Button(mainframe, text= 7, style="Botones_numeros.TButton", command= lambda: ingresarValores("7"))
button8 = ttk.Button(mainframe, text= 8, style="Botones_numeros.TButton", command= lambda: ingresarValores("8"))
button9 = ttk.Button(mainframe, text= 9, style="Botones_numeros.TButton", command= lambda: ingresarValores("9"))

buttonBorrar = ttk.Button(mainframe, text= chr(9003), style="Botones_borrar.TButton", command = lambda: borrar())
buttonBorrarTodo = ttk.Button(mainframe, text= "C", style="Botones_borrar.TButton", command = lambda: borrarTodo())
buttonParantesis1 = ttk.Button(mainframe, text= "(", style="Botones_restantes.TButton", command= lambda: ingresarValores("("))
buttonParantesis2 = ttk.Button(mainframe, text= ")",style="Botones_restantes.TButton", command= lambda: ingresarValores(")"))
buttonPunto = ttk.Button(mainframe, text= ".",style="Botones_restantes.TButton", command= lambda: ingresarValores("."))

buttonDivision = ttk.Button(mainframe, text= chr(247),style="Botones_restantes.TButton", command= lambda: ingresarValores("/"))
buttonMultiplicacion = ttk.Button(mainframe, text= "x",style="Botones_restantes.TButton", command= lambda: ingresarValores("*"))
buttonResta = ttk.Button(mainframe, text= "-",style="Botones_restantes.TButton", command= lambda: ingresarValores("-"))
buttonSuma = ttk.Button(mainframe, text= "+",style="Botones_restantes.TButton", command= lambda: ingresarValores("+"))

buttonIgual = ttk.Button(mainframe, text= "=",style="Botones_restantes.TButton", command= lambda: ingresarValores("="))
buttonRaizCuadrada = ttk.Button(mainframe, text= "√",style="Botones_restantes.TButton", command= lambda: raizCuadrada())

#Colocar botones

buttonParantesis1.grid(column= 0, row= 2,sticky=(W, N, E ,S))
buttonParantesis2.grid(column= 1, row=2,sticky=(W, N, E ,S))
buttonBorrarTodo.grid(column= 2, row=2,sticky=(W, N, E ,S))
buttonBorrar.grid(column= 3, row=2,sticky=(W, N, E ,S))

button7.grid(column =0, row = 3,sticky=(W, N, E ,S))
button8.grid(column =1, row = 3,sticky=(W, N, E ,S))
button9.grid(column =2, row = 3,sticky=(W, N, E ,S))
buttonDivision.grid(column =3, row = 3,sticky=(W, N, E ,S))

button4.grid(column =0, row = 4,sticky=(W, N, E ,S))
button5.grid(column =1, row = 4,sticky=(W, N, E ,S))
button6.grid(column =2, row = 4,sticky=(W, N, E ,S))
buttonMultiplicacion.grid(column =3, row = 4,sticky=(W, N, E ,S))

button1.grid(column =0, row = 5,sticky=(W, N, E ,S))
button2.grid(column =1, row = 5,sticky=(W, N, E ,S))
button3.grid(column =2, row = 5,sticky=(W, N, E ,S))
buttonSuma.grid(column =3, row = 5,sticky=(W, N, E ,S))

button0.grid(column =0, row = 6, columnspan = 2,sticky=(W, N, E ,S))
buttonPunto.grid(column =2, row = 6,sticky=(W, N, E ,S))
buttonResta.grid(column =3, row = 6,sticky=(W, N, E ,S))

buttonIgual.grid(column =0, row = 7, columnspan=3 ,sticky=(W, N, E ,S))
buttonRaizCuadrada.grid(column =3, row = 7,sticky=(W, N, E ,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady= 19.3, padx= 8.8, pady= 1)
    
    
window.mainloop()