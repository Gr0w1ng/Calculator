from tkinter import *
from tkinter import ttk
from math import *

root  = Tk()
root.title("Calculator")
root.geometry("+500+80")

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column = 0, row = 0)

estilosLabel1 = ttk.Style()
estilosLabel1.configure("label1.TLabel", font= "arial 15", anchor = "E") 

estilosLabel2 = ttk.Style()
estilosLabel2.configure("label2.TLabel", font= "arial 40", anchor = "e") 

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="label1.TLabel")
label_entrada1.grid(column = 0, row =0, columnspan=4,sticky=(W, E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable = entrada2,style="label2.TLabel")
label_entrada2.grid(column = 0, row =0, columnspan=4,sticky=(W,E))

#Estilos de los botones

estilosBotonesNumeros = ttk.Style()
estilosBotonesNumeros.configure("Botones_numeros.TButton", font="arial 22", width="5", background="#FFFFFF",relief="flat")

estilosBotonesBorrar = ttk.Style()
estilosBotonesBorrar.configure("Botones_borrar.TButton", font="arial 22", width="5", background="#CECECE",relief="flat")
estilosBotonesBorrar.map("Botones_borrar.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])

estilosBotonesRestantes = ttk.Style()
estilosBotonesRestantes.configure("Botones_restantes.TButton", font="arial 22", width="5", background="#CECECE",relief="flat")

#Botones

button0 = ttk.Button(mainframe, text= 0, style="Botones_numeros.TButton")
button1 = ttk.Button(mainframe, text= 1, style="Botones_numeros.TButton")
button2 = ttk.Button(mainframe, text= 2, style="Botones_numeros.TButton")
button3 = ttk.Button(mainframe, text= 3, style="Botones_numeros.TButton")
button4 = ttk.Button(mainframe, text= 4, style="Botones_numeros.TButton")
button5 = ttk.Button(mainframe, text= 5, style="Botones_numeros.TButton")
button6 = ttk.Button(mainframe, text= 6, style="Botones_numeros.TButton")
button7 = ttk.Button(mainframe, text= 7, style="Botones_numeros.TButton")
button8 = ttk.Button(mainframe, text= 8, style="Botones_numeros.TButton")
button9 = ttk.Button(mainframe, text= 9, style="Botones_numeros.TButton")

buttonBorrar = ttk.Button(mainframe, text= chr(9003), style="Botones_borrar.TButton")
buttonBorrarTodo = ttk.Button(mainframe, text= "C", style="Botones_borrar.TButton")
buttonParantesis1 = ttk.Button(mainframe, text= "(", style="Botones_restantes.TButton")
buttonParantesis2 = ttk.Button(mainframe, text= ")",style="Botones_restantes.TButton")
buttonPunto = ttk.Button(mainframe, text= ".",style="Botones_restantes.TButton")

buttonDivision = ttk.Button(mainframe, text= chr(247),style="Botones_restantes.TButton")
buttonMultiplicacion = ttk.Button(mainframe, text= "x",style="Botones_restantes.TButton")
buttonResta = ttk.Button(mainframe, text= "-",style="Botones_restantes.TButton")
buttonSuma = ttk.Button(mainframe, text= "+",style="Botones_restantes.TButton")

buttonIgual = ttk.Button(mainframe, text= "=",style="Botones_restantes.TButton")
buttonRaizCuadrada = ttk.Button(mainframe, text= "√",style="Botones_restantes.TButton")

#Coloca botones en pantalla

buttonParantesis1.grid(column= 0, row= 2)
buttonParantesis2.grid(column= 1, row=2)
buttonBorrarTodo.grid(column= 2, row=2)
buttonBorrar.grid(column= 3, row=2)

button7.grid(column =0, row = 3)
button8.grid(column =1, row = 3)
button9.grid(column =2, row = 3)
buttonDivision.grid(column =3, row = 3)

button4.grid(column =0, row = 4)
button5.grid(column =1, row = 4)
button6.grid(column =2, row = 4)
buttonMultiplicacion.grid(column =3, row = 4)

button1.grid(column =0, row = 5)
button2.grid(column =1, row = 5)
button3.grid(column =2, row = 5)
buttonSuma.grid(column =3, row = 5)

button0.grid(column =0, row = 6, columnspan = 2, sticky = (W , E))
buttonPunto.grid(column =2, row = 6)
buttonResta.grid(column =3, row = 6)

buttonIgual.grid(column =0, row = 7, columnspan=3 , sticky = (W , E))
buttonRaizCuadrada.grid(column =3, row = 7)

for child in mainframe.winfo_children():
    child.grid_configure(ipady= 10, padx= 1, pady= 1)

root.mainloop()