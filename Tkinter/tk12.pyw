#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 23/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

root = Tk()
root.geometry("300x300+500+300") 
root.title("Crear Barra de Menu")
root.config()

#Creamos el Menu
menubar = Menu(root)
#Agregamos el Menu a la Raíz
root.config(menu=menubar)

#Creamos los submenus
archivo = Menu(menubar, tearoff=0) #tearoff=0 quitar opcion default
#Agregamos los comandos al submenu Archivo
archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="Cerrar", command=root.quit)

editar = Menu(menubar, tearoff=0)
editar.add_command(label="Copiar")
editar.add_command(label="Pegar")

ayuda = Menu(menubar,tearoff=0)
ayuda.add_command(label="Acerca de")

#Agregamos los submenus al Menu
menubar.add_cascade(label="Archivo", menu=archivo)
menubar.add_cascade(label="Editar", menu=editar)
menubar.add_cascade(label="Ayuda", menu=ayuda)

root.mainloop()