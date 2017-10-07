#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 21/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

def calcular():
	far = (1.8)*c.get() + 32
	f.set(round(far,2))

root = Tk()
root.geometry("300x300+500+300") # +500+300 es para indicar en que parte de la pantalla se ubicara
root.title("Crear Escala")
root.config(bd=10)
#variables
f = IntVar()
c = IntVar()


#Escala
s = Scale(root, from_=0, to=100, label="Grados Centrigrados", orient=HORIZONTAL
          ,length=200,variable=c,tickinterval=10)
s.pack()


Label(root,text="Grados fahrenheit").pack()
Entry(root,textvariable=f,state="disabled").pack()
Button(root,text="Calcular", command=calcular).pack()

root.mainloop()