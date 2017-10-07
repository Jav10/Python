#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 19/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *
from tkinter import ttk

#Es la ríaz
root = Tk()

#Algunas propiedades
root.title("Crear Ventana y Marco") # Título de la ventana
root.resizable(0,0) #Poder cambiar el tamaño
root.iconbitmap('X-Wing_-_02_35411.ico') #Icono de la ventana
root.geometry('300x300') #Medida de la ventana
root.config(cursor="pirate",bg="beige",bd=10,relief="ridge") #Configuración de la raíz

#Frame
frame = Frame(root, width=200, height=200) #Creando el marco
frame.config(cursor="spider",bg="lightblue") #Configuración del marco
frame.pack(side="top", anchor="w") #Empaqueta el elemento en la raíz si no, no se puede mostrar, paramestros para posición
# frame.pack(fill='x' o 'y' o 'both', expand=1 o 0) rellenar y expandir (se usan con fill=y 0 both) a las dimenciones del padre

#Loop principal
root.mainloop() #ciclo para que inicien los procesos y capte los eventos
