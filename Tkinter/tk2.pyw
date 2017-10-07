#GUI con TKinter
#Autor: Javier Arturo Hernández Sosa
#Fecha: 19/Sep/2017
#Descripcion: Curso Python FES Acatlán

from tkinter import *

#Root
root = Tk()
root.title("Crear Etiquetas")
root.geometry("500x500")

#Variables dinámicas
texto = StringVar()
texto.set("Texto dinámico!!!!")
#Frame
frame = Frame(root, width=400, height=400)
frame.place(x=50,y=50)
frame.config(bg="pink")

#Label
label = Label(frame, text="Curso Python GUI") #Etiqueta
label.place(x=80,y=10) #Empaquetar
label.config(bg="lightblue", fg="yellow", font=("Arial Black", 18)) #Configuración
label.config(textvariable=texto) 
'''
Configuración
bg = background
fg = foreground
font(fuente,tamaño)
'''

imagen = PhotoImage(file="200.gif") #Cargamos la variable

label2 = Label(root, image=imagen)
label2.place(x=150,y=150)


#Bucle principal
root.mainloop()
