#Tipos de datos compuestos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 3/Sep/2017
#Descripcion: Curso Python FES Acatlán

#listas
'''
	Lista de valores separados por comas entre corchetes, puede contener diferentes tipos de datos.
	Las listas son tipos mutables (Las cadenas de texto son inmutables)
'''
lista = ["Juan",16,"Pedro",17]
print(lista)
print(type(lista))

#indexear listas
print(lista[0]) #Primer elemento
print(lista[-1]) #Último elemento
print(lista[2:]) #Rebanando listas

concat = lista + ["Julio",16] #concatenación
print(concat)
concat[0] = "JuanFran" #Usando mutabilidad, cambiando un valor de la lista
print(concat)

#Método append - agregando al final de la lista
concat.append("Fulgore")
concat.append(18)
#Reemplazar valores
concat[2:4] = ['Jav',19]
print(concat)
#Borrando elementos
concat[4:6] = []
print(concat)
#Borrando listas
concat[:] = []
print(concat)
#Método funcion len (tamaño)
print(len(lista))
#Anidando listas
lista1 = ['Jav','Arturo']
lista2 = [16,18]
listaFinal = [lista1,lista2]
print(listaFinal)
print(listaFinal[0][1])

#Tuplas
'''
	Una tupla es un objeto inmutable, eso quiere decir que no se pueden cambiar sus elementos
	Se usan parentesis para declararla, sus elementos van separados por comas 
	y pueden contener varios tipos de dato
	Son inmutables aunque pueden contener elementos mutables como listas
'''

#Declarando tupla
t = () #Tupla vacia
t = 4, #Tupla con un elemento
t = (3,"Hi",9)
print(type(t))
x,y,z = t #Desempaquetando secuencias
print(x,y,z)

#Conjuntos
'''
	Colección no ordenada y sin elementos repetidos
	Soportan operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica
	Se declaran con llaves {} o con set()
'''

animales = {'perro', 'vaca', 'raton', 'conejo', 'aguila', 'vaca', 'conejo'}
animales2 = {'conejo', 'burro', 'ballena', 'gato', 'perico', 'perro', 'gato', 'ballena'}
animales3 = {'perro','conejo','aguila'}
print(animales) #Se eliminan los elementos repetidos
#Operaciones entre conjuntos
print("cardinalidad en animales: ",len(animales)) #cardinalidad
print('cocodrilo' in animales2) #Comprobando pertenencia
print(animales == animales2) #Igualdad entre conjuntos, el orden no importa
print(animales3.issubset(animales)) #Subconjunto, animales3 subconjunto de animales?
print(animales3.issubset(animales) and animales3!=animales) #Subconjunto propio
print(animales.union(animales2)) #Union ->  animales | animales2
print(animales.intersection(animales2)) #Intesección -> animales & animales2
print(animales - animales2) #Diferencia
print(animales ^ animales2) #Diferencia Simétrica (todo menos la intesección)
#Ver Ejemplo ven en el sitio

#Diccionarios
'''
	Son una colección no ordenada de valores a los cuales se pueden
	acceder mediante una clave, la clave es única.
	No hay forma directa de acceder mediante su valor y un mismo valor pueden
	estar accinado en varias claves
	(arrays asociativos o tablas hash)
'''
#Declarar diccionario
dic = {} #Diccionario vacio
dic = {"nombre":"Arturo","apellido":"Hernández"}
print(dic)
dic['animal'] = "Lobo" #Agregando valores al diccionario
print(dic)
del dic["animal"] #Borrando valores
print(dic)
print(dic.keys()) #Listando las llaves
print('name' in dic) #Verificando llaves
dic2 = dict(arturo=4345,pepe=2363,jose=2938) #crea un diccionario con dict
print(dic2)
#Iterando
for i in lista: #interando listas o tuplas 
	print(i)
	
for i in animales: #iterando conjuntos
	print(i)
	
for i in dic:      #Itera las claves y las usamos para ver los valores
	print(dic[i])	

for clave,valor in dic.items():   #obtenemos los valores como pares de tuplas clave:valor
	print(str(clave)+" : "+str(valor))	
	
#verificar si una clave se encuentra en el diccionario
if 'apellido' in dic:     #Con palabra reservada in
	print(dic['apellido'])	
