#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 20/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

root = Tk()
root.title("Campo de texto")

texto = Text(root) #Campo de texto
texto.place(x=0,y=0) #Empaquetar
texto.config(width=50, height=50,padx=5,pady=5, font=("arial",12), selectbackground="pink", selectforeground="blue") #tamaño en caracteres width y height
'''
	selectbackground = fondo al seleccionar
	selectforeground = color del texto seleccionado
'''

root.mainloop()