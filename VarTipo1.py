#Variables y tipos de datos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 28/Ago/2017
#Descripcion: Curso Python FES Acatlán

#Tipos de datos 
numero = 5 #Operador de asignación
numero2 = 19
numeroFlotante = 25.0
cadena = "Hola Mundo"
boleano1 = True
boleano2 = False
complejo1 = 5 - 3j
complejo2 = 2 + 5j
#Operaciones Comunes +,-,/,//,%,*,**
print(numero+numeroFlotante)
print(numero-numero2)
print(19/5) #División Clásica regresa punto flotante
print(19//3) #División Entera omite fracción
print(19%5) #Operador Módulo regresa residuo
print(numero*numero2)
print(3**2) #Potencia 3 elevado a la 2
#Operaciones con cadenas
print(cadena*5)
print(cadena+cadena) #Concatenación
print(cadena+" "+"Continua")
#Booleanos
print(boleano1)
print(boleano2)
#Operadores lógicos
print(boleano1 & boleano2) #and
print(boleano1 & boleano1)
print(boleano1 | boleano2) #or
print(boleano2 | boleano2)
print(not boleano1)
print(boleano1 ^ boleano2) #xor verdadero si tienen valores diferentes, falso si son iguales
#Operadores de comparación
print(2==3)
print(6==6)
print("Hola"!="hola")
print("hola"<"dromedario")
print("hola">"zromedario")
print("Hormiga">="Hola")
print("Cono"<="Vaca")
#Conversion de tipos
#Para saber el tipo de datos type()
print(type("Oso"))
print(type(int(5.89)))
print(type(5.89))
print(type(str(567)))
#Esto es un error print(int("oso"))
#Complejos
print(complejo1 + complejo2)
