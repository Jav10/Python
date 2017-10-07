#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 20/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

def opcion():
	r = op.get()
	if(r == 1):
		n = "Python Excelente Elección!"
	elif(r == 2):
		n = "Java Mala Elección"
	else:
		n = "R Buena Elección"
	etiqueta.config(text="{}".format(n))

root = Tk()
root.geometry("150x70")
root.title("Crear Radio Boton")

op = IntVar()

etiqueta2 = Label(root, text="¿Cuál Lenguaje Prefieres?")
etiqueta2.grid(row=0,column=0,columnspan=3)

#Radio Botones ->value diferente para crear independencia 
rBoton = Radiobutton(root, text="Python", variable=op, value=1, command=opcion)
rBoton2 = Radiobutton(root, text="Java", variable=op, value=2, command=opcion)
rBoton3 = Radiobutton(root, text="R", variable=op, value=3, command=opcion)

rBoton.grid(row=1,column=0)
rBoton2.grid(row=1,column=1)
rBoton3.grid(row=1,column=2)

etiqueta = Label(root)
etiqueta.grid(row=2,column=0,columnspan=3)

root.mainloop()