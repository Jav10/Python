#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 20/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

#Definición de funciones
def suma():
	r.set(x.get() + y.get())

def multi():
	r.set(x.get() * y.get())
	
def resta():
	r.set(x.get() - y.get())	

def dividir():
	r.set(x.get() / y.get())

#Ventana raíz	
root = Tk()
#Configuración raíz
root.geometry("300x300")
root.title("Botones y funciones")
root.config(bd=15)

#variables para widgets
x = DoubleVar()
y = DoubleVar()
r = StringVar()

#Entradas y resultado
numero1 = Entry(root,textvariable=x, justify="center")
numero2 =Entry(root,textvariable=y, justify="center")
resultado = Entry(root, textvariable=r, justify="center", state="disabled") #stated para bloquear el widget

#Empaquetado
numero1.grid(row=0,column=0,padx=5,pady=5)
numero2.grid(row=0,column=1,padx=5,pady=5)
resultado.grid(row=3,column=0, columnspan=2,padx=5,pady=5) #Expandir columnas

#Botones
sumar = Button(root, text="Sumar", command=suma) #botones, command para pasar funcion
sumar.grid(row=1,column=0,padx=5,pady=5)

multiplicar = Button(root, text="Multiplicar", command=multi)
multiplicar.grid(row=1,column=1,padx=5,pady=5)

restar = Button(root, text="Restar", command=resta)
restar.grid(row=2,column=0,padx=5,pady=5)

dividir = Button(root, text="Dividir", command=dividir)
dividir.grid(row=2,column=1,padx=5,pady=5)

#loop principal
root.mainloop()
