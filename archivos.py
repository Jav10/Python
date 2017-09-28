#Manejo de Archivos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 24/Sep/2017
#Descripcion: Curso Python FES Acatlán

# C:\Users\Jahs\Desktop\Hola.py -> "C:/Users/Jahs/Desktop/Hola.py"

#C:/Users/Jahs/Documents/Github/Curso Python/copia.png

#Abrir ficheros
# open(nombre_de_archivo, modo)
fichero = open("texto.txt","r")
#Propiedades del objeto file
'''
fichero.closed: Retorna True si el archivo esta cerrado y False si no.
fichero.mode: Retorna el modo de apertura.
fichero.name: Retorna el nombre del archivo.
fichero.encoding: Retorna la codificación de caracteres del archivo.
'''
print(fichero.mode)
print(fichero.name)
print(fichero.encoding)
print(fichero.closed)
'''	
	Modos de apertura
r: Solamente cuando el archivo será leido.
w: Para escribir en el archivo, si no existe será creado
   si existe sera borrado su contenido. 
a: Abre el archivo para agregar información, cualquier
   dato escrito en el archivo será agregado al final automáticamente.
r+: Abre el archivo tanto para leerlo como para escribirlo.
w+: Abre el archivo tanto para leerlo como para escribirlo.si no existe será creado
   si existe sera borrado su contenido.
a+: Abre el archivo tanto para leerlo como para escribirlo.

b: Se argrega para abrir archivos que no sean de texto, y se abren en modo binario. (objetos bytes)
El argumento modo es opcional si no se agrega por default el archivo se abre con 'r'   
'''
#Métodos
'''
fichero.read(cantidad): Lee la cantidad indicada de caracteres si no se usa
			se lee el archivo completo.
fichero.readline():  Lee una sóla linea del archivo y si regresa una linea vacia 
					 se debe a que es el final del archivo.
fichero.readlines(): Lee todas las lineas de un archivo.
fichero.tell(): Indica la posición actual en el archivo en bytes.
fichero.seek(): Cambia la posición actual del archivo
fichero.close(): Cierra el archivo
'''
print(fichero.tell()) #Vemos en que posición se encuentra el archivo - inicio
print("Método READ")
print(fichero.read()) #Leemos todo el archivo
print(fichero.tell()) #Vemos en que posición se encuentra - final
fichero.seek(0) #Cambiamos la posición al inicio
print("Método READLINES")
s = fichero.readlines() #Se crea una lista con las lineas del archivo
print(s) #Imprimimos la lista, también se podría con un FOR
fichero.seek(0) #Cambiamos la posicición al inicio, porque si no ya no lee nada
print("Método READLINE") #Leemos linea por linea
for i in fichero:
    print(fichero.readline(), end='')

#También puede usarse
fichero.seek(0)
print("Iterar con FOR")
for lineas in fichero:
    print(lineas, end='\n')
#Cerrar el archivo
fichero.close() #cierra el archivo

#Otro modo de abrir un archivo
print("Abrir con with")
with open("texto.txt","r") as archivo:
    print(archivo.read())
print(archivo.closed)
