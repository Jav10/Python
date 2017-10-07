#Funciones
#Autor: Javier Arturo Hernández Sosa
#Fecha: 6/Sep/2017
#Descripcion: Curso Python FES Acatlán

#Funciones
'''
	Usamos la palabra reservada 'def' para definir funciones seguido del nombre de esta.
'''
def saludo():
	"""Funcion manda un saludo por consola"""
	print("Hola Mundo")

#Llamar función	
saludo()

#Return	
def retorno():
	"""Regresa un valor usando la palabra reservada return-> x*y"""
	x = 10
	y = 10
	return x*y

print(retorno())

#Parámetros
def param(x):
	"""Esta función usa parámetros (cubo de un número)"""
	res = x*x*x
	return res	

print(param(5))

#Podemos asginar una funcion a una variable
parametro = param
print(parametro(10))

#Podemos asignar el resultado de una función a una variable
resultado = param(20)
print(resultado)

#Parámetros obligatorios y opcionales
def multip(x,y=1, z=1):
	"""Multiplica 3 números"""
	resultado = x*y*z
	return resultado
	
#Error multip() si se tiene un parámetro obligatorio es forsozo agregarlo
print(multip(5)) #5, si no se pasan los valores opcionales, se activan los valores por defecto
print(multip(5,2)) #10
print(multip(5,2,2)) #20

#argumento posicional y luego nombrados esto sería un error multip(x=5,4,6)
multip(3,y=3,z=4)

#Las funciones pueden recivir un número arbitrario de argumentos y diccionarios	 
def cadenas(*tupla):
	for i in tupla:
		print(i)
		
cadenas("palabra1","palabra2","palabra3","palabra4")

def diccionario(**dic):
	for i,v in dic.items():
		print("clave-> ",i,":","Valor->",v)
		
diccionario(perro="fido", gato="pelusa", conejo="cone")		

#Todo junto, parámetros arbitrarios
def cadic(valor,*tupla,**dic):
	print(valor)
	for i in tupla:
		print(i)
	for i,v in dic.items():
		print("clave-> ",i,":","Valor->",v)
		
cadic(5,"palabra1","palabra2","palabra3","palabra4",perro="fido", gato="pelusa", conejo="cone")		