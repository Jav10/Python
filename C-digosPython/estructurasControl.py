#Estructuras de Control
#Autor: Javier Arturo Hernández Sosa
#Fecha: 1/Sep/2017
#Descripcion: Curso Python FES Acatlán

#sentencia IF,ELSE y ELIF
edad = 10
if(edad<18):
	print("Eres un niño todavía")
elif(edad>=18 and edad<40):
	print("Eres un adulto")
elif(edad>=40 and edad<70):
	print("Ya estas viejo")
else:
	print("Ya te pasaste de maduro")

#sentencia WHILE
x = 0
while(True):
	x = x + 1
	if(x==3):
		print("Nos brincamos el 3")
		continue
	elif(x==8):
		print("En el 8 rompemos el ciclo")
		break
	print(x)

'''Función RANGE
	range(inicio,final,incremento) Genera una progreción aritmética
	range(10) 0 a 9
	range(5,10) 5 a 9
	range 5,10,2) 5 a 9 de 2 en 2
	'''
#sentencia FOR
for i in range(1,10,1):
	if(i==3):
		print("Se brinca el 3")
		continue
	elif(i==8):
		print("Rompiendo for")
		break
	print(i)	

#FOR y WHILE pueden tener una cláusula ELSE
'''En el caso del for la cláusula se ejecuta cuando finaliza el el for pero no cuando termina por un break
En el caso de while la cláusula se ejecuta cuando la condición se vuelve false
'''
for i in "Hola":
	print(i)
else:
	print("Termino la iteración del for")
y = 3
while(y<10):
	y = y + 1
	if(y==8):
		print("Se rompe el ciclo")
		break
	print(y)
else:
	print("La condición se rompio")		
