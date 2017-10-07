#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 21/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

def pedido():
	orden = ""
	if(ham.get()):
		orden += "Hamburguesa"
	else:
		orden += "Sin Hamburguesa"
	if(pap.get()):
		orden += " Con Papas"
	else:
		orden += " Sin Papas"
	if(ref.get()):
		orden += " Con Refresco"
	else:
		orden += " Sin Refresco"
	Orden.config(text=orden)
	
root = Tk()
root.geometry("250x200+500+300") # +500+300 es para indicar en que parte de la pantalla se ubicara
root.title("Crear Boton verificador")
root.config(bd=10)

ham = IntVar()
pap = IntVar()
ref = IntVar()

Label(root,text="Pedido de paquete").pack()

#boton de verificación
'''
onvalue = valor seleccionado
offvalue = valor sin selección
'''
cBoton = Checkbutton(root, text="Hamburguesa", variable=ham, onvalue=1, offvalue=0, command=pedido)
cBoton2 = Checkbutton(root, text="Papas", variable=pap, onvalue=1, offvalue=0, command=pedido)
cBoton3 = Checkbutton(root, text="Refresco", variable=ref, onvalue=1, offvalue=0, command=pedido)

cBoton.pack()
cBoton2.pack()
cBoton3.pack()

Orden = Label(root)
Orden.pack()

root.mainloop()