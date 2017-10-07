#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 21/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

def on():
	if(p.get() != ""):
		lista.insert(END,p.get())
		p.set("")

def borrar():
	b = lista.curselection()
	if(b != ""):
		lista.delete(b)
	
root = Tk()
root.geometry("300x300+500+300") # +500+300 es para indicar en que parte de la pantalla se ubicara
root.title("Crear Caja de lista")
root.config(bd=10)

p = StringVar()

Label(root,text='Persona:').pack()
Entry(root, textvariable=p).pack()
#Lista
lista = Listbox(root,activestyle="underline") #activestyle para el estilo de linea al seleccionar
lista.pack()

Button(root,text="Agregar",command=on).pack()
Button(root,text="Borrar",command=borrar).pack()

root.mainloop()