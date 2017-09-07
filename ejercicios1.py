#Ejercicios 1
#Autor: Javier Arturo Hernández Sosa
#Fecha: 6/Sep/2017
#Descripcion: Curso Python FES Acatlán

#Ver si un número es par o impar
numero = int(input("Dame un número: "))
if((numero%2) == 0):
	print("El numero ingresado es par.")
	
else:
	print("El número ingresado es impar")	
	
#Saber si una cadena es Palíndromo
cadena = input("Dame una cadena: ")

nCadena = cadena.replace(" ","")
for i in range(len(nCadena)):
	if(nCadena[i]==nCadena[-(i+1)]):
		pass
	else:
		print("No es paíndromo")
		break
else:
        print("Si es palíndromo")        

#Multiplicación de vectores
tam = int(input("Ingresa la dimención de los vectores: "))
vec1 = []
vec2 = []
for i in range(2):
        x = 0
        while(x<tam):
                if(i==0):
                        valor = int(input("Dame los valores del vector 1: "))
                        vec1.append(valor)
                elif(i==1):
                        valor = int(input("Dame los valores del vector 2: "))
                        vec2.append(valor)
                x = x+1        
m = 0
for i in range(tam):
        m = m + (vec1[i] * vec2[i])

print(f"El resultado de la multiplicación de los vectores es: {m}")

#Multiplicación de matrices 2x2
lista1 = [[1,2],[2,3]]
lista2 = [[3,3],[3,3]]
lista3 = [[0,0],[0,0]]
print("Matriz 1")
print(lista1)
print("Matriz 2")
print(lista2)
for i in range(2):
    for j in range(2):
        for k in range(2):
            lista3[i][j] = lista3[i][j]+(lista1[i][k] * lista2[k][j])
else:
    print("Resultado de la multiplicación: ")
    print(lista3)                                          
                        
