#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 21/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

def enviar():
	n = valor.get()
	valor2.set(n)
	
	
root = Tk()
root.geometry("300x300+500+300") # +500+300 es para indicar en que parte de la pantalla se ubicara
root.title("Crear Spinbox")
root.config(bd=10)

valor = IntVar()
valor2 = IntVar()

Label(root,text="Calificate.").pack()
spin = Spinbox(root, from_=50, to=100, increment=5,textvariable=valor)
'''
	También se puede usar values=('Gato', 'Perro', 'Rana') y estos seran los valores que aparecen
'''
spin.pack()

Button(root,text="Enviar",command=enviar).pack()
l = Label(root,textvariable=valor2).pack()

root.mainloop()