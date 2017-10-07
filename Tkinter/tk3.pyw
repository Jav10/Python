#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 19/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

#ventana principal
root = Tk()
root.title("Crear Entradas")
root.geometry("300x300")

#Etiquetas
Nombrelb = Label(root, text="Nombre - name: ")
Apellidolb = Label(root, text="Apellido: ")

Nombrelb.grid(row=0, column=0,sticky="e") #grid celdas para ubicar elementos
Apellidolb.grid(row=1,column=0,sticky="e") #sticky para justificar por default es center

Nombrelb.config(fg="blue", font=("Arial Black", 12)) #Configuración
Apellidolb.config(fg="blue", font=("Arial Black", 12))

#Entrada
nombre = Entry(root)
nombre.grid(row=0,column=1)
contrasena = Entry(root)
contrasena.grid(row=1,column=1)
contrasena.config(show="*") #Mostrar otros caracteres en vez de lo escrito

#bucle de la aplicación
root.mainloop()