#GUI con TKinter - Procesador de Texto
#Autor: Javier Arturo Hernández Sosa
#Fecha: 23/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from io import open

#Variables de control
ruta = "" #Variable para verificar archivo
g = "" #Variable para verificar borrado

#Funciones del Menu
	#Archivo
def nuevo():
	if(texto.edit_modified() == 0):
		texto.delete(1.0,END)
	elif(texto.edit_modified() == 1):
		r = mb.askquestion("Guardar", "¿Quiere guardar el archivo?")
		if(r == 'yes'):
			guardar() #Verificar que no guarde si regresa cancelar BORRAR
			if(g != None):
				texto.delete(1.0,END)
				texto.edit_modified(False)
		else:
			texto.delete(1.0,END)
			texto.edit_modified(False)
		
def abrir():
	nuevo()
	global ruta
	try:
		ruta = fd.askopenfilename(title="Abrir",filetypes = (("Fichero texto","*.txt"),("Archivos Python","*.py"),("Archivos Python","*.pyw"),("Archivos C","*.c"),("Archivos Cplusplus","*.cpp"),("Todos los ficheros","*.*")))		
	except TclError:
		mb.showwarning("Error", "Ocurrio un error y no se puede abrir el archivo")
	if(ruta != ""):
		archivo = open(ruta, "r+")
		contenido = archivo.read()
		texto.delete(1.0,END)
		texto.insert(INSERT, contenido)
		archivo.close()
		texto.edit_modified(False)

def guardar():
	global ruta
	if(texto.edit_modified() == 0):
		mb.showinfo("Información", "Su información esta guardada.")
	elif(texto.edit_modified() == 1):
		if(ruta != ""):
			contenido = texto.get(1.0,END)
			archivo = open(ruta, "w+")
			archivo.write(contenido)
			archivo.close()
			texto.edit_modified(False)
			texto.edit_reset()
		elif(ruta == ""):
			guardarComo()
			
def guardarComo():
	archivo = fd.asksaveasfile(title="Guardar como",mode="w+",defaultextension=".py",filetypes = (("Fichero texto","*.txt"),("Archivos Python","*.py"),("Archivos Python","*.pyw"),("Archivos C","*.c"),("Archivos Cplusplus","*.cpp"),("Todos los ficheros","*.*")))
	global g
	g = archivo
	if archivo is not None:
		contenido = texto.get(1.0,END)
		archivo.write(contenido)
		archivo.close()
	
	#Editar
def undo():
	texto.event_generate("<<Undo>>")
def redo():
	texto.event_generate("<<Redo>>")
def cortar():
	texto.event_generate("<<Cut>>")	
def copiar():
	texto.event_generate("<<Copy>>")	
def pegar():
	texto.event_generate("<<Paste>>")	
	
	#Ayuda
def Ade():
	vHija = Toplevel(root)
	vHija.geometry("300x50+500+500") 
	Label(vHija,text="Procesador de Texto v1.0").pack()
	Label(vHija,text="© 2017 - JAHS - Todos los derechos reservados").pack()

#Manejar cuando se cierra el programa
def cerrar():
	if(texto.edit_modified() != 0):
		r = mb.askquestion("Guardar", "¿Quiere guardar el archivo antes de salir?")
		if(r == 'yes'):
			guardar() #Verificar que no guarde si regresa cancelar BORRAR
			if(g != None):
				root.destroy()
		else:
			root.destroy()
	else:
		root.destroy()
	

root = Tk()
root.geometry("800x500+250+250") 
root.title("Procesador de Texto")
root.resizable(0,0)
root.protocol("WM_DELETE_WINDOW", cerrar)

#scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
#Cosas para implementar
'''
widget.edit_reset() #Para limpiar la pila de undo cuando se guarda el documento
widget.event_info() #Para ver que eventos tiene por defecto

Código sin usar para crear copiar
try:
	copia = texto.selection_get() #VERIFICAR
except TclError:
	mb.showinfo("Información", "No hay nada en el portapapeles")
	print(texto.event_info()	)
'''

#Creamos el Menu
menubar = Menu(root)

#Agregamos el Menu a la Raíz
root.config(menu=menubar)

#Creamos los submenus
archivo = Menu(menubar, tearoff=0) #tearoff=0 quitar opcion default
	#Agregamos los comandos al submenu Archivo
archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_command(label="Guardar", command=guardar)
archivo.add_command(label="Guardar como", command=guardarComo)
archivo.add_separator()
archivo.add_command(label="Cerrar", command=root.quit)
	#Agregamos los comandos al submenu Editar
editar = Menu(menubar, tearoff=0)
editar.add_command(label="Deshacer", command=undo)
editar.add_command(label="Rehacer", command=redo)
editar.add_command(label="Cortar", command=cortar)
editar.add_command(label="Copiar", command=copiar)
editar.add_command(label="Pegar", command=pegar)
	#Agregamos los comandos al submenu Editar
ayuda = Menu(menubar,tearoff=0)
ayuda.add_command(label="Acerca de", command=Ade)

#Agregamos los submenus al Menu
menubar.add_cascade(label="Archivo", menu=archivo)
menubar.add_cascade(label="Editar", menu=editar)
menubar.add_cascade(label="Ayuda", menu=ayuda)

#Texto
texto = Text(root)
texto.pack(fill=BOTH, expand=1)
texto.config(font=("arial",12),bg="beige",maxundo=20, yscrollcommand = scrollbar.set)
scrollbar.config( command = texto.yview )

root.mainloop()

