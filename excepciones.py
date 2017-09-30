#Manejo de Archivos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 24/Sep/2017
#Descripcion: Curso Python FES Acatlán

'''
Los errores de sintaxis, también conocidos como errores de interpretación.
'''

# prinCt("Hola") Ocurren cuando escribimos mal algo dentro del código

'''
Excepciones, son errores que ocurren durante la ejecución aunque
la sintaxis sea correcta, pero estos se pueden manejar para que
el programa no termine inesperadamente.
'''

'''
Algunas excepciones comunes:

ZeroDivisionError: división por cero
NameError: Variable no definida
TypeError: Error de conversion de tipo implicita
ImportError: Error cuando carga una libreria
IndexError: Cuando una secuencia esta fuera de rango
OverflowError: Cuando una operación aritmética es demaciado grande para representarla
KeyboardInterrupt: Cuando el usuario interrumpe con 'control-c' para windows
OSError: Ocurre cuando la función de sistema regresa un error, como
         no poder abrir un archivo o el disco de escritura esta lleno
ETC...
'''

#Manejando Excepciones
#Una excepción
try:
	x = int(input("Dame un número"))
	
except ValueError:
	print("El valor que ingresaste no es un número.")

#Multiples excepciones
try:
	x = int(input("Dame un número"))
	resultado = 5/x
except ValueError:
	print("El valor que ingresaste no es un número.")
except ZeroDivisionError:
	print("División entre cero.")
#También pueden colocarse varios errores en un solo except
'''
	except (ValueError,ZeroDivisionError):
		print("Ocurrio un error, pruebe a ingresar un valor que no sea un cero , una letra o un signo.")
'''	

#De igual manera podemos usar except sin parámetros
try:
	x = int(input("Dame un número"))
	resultado = 5/x
except:
	print("Ocurrio un error")

'''
 Aquí podemos capturar cualquier error que ocurrar pero no sabremos de que tipo
 y esto podría ocultar errores de programación.
'''	
#bloque ELSE
'''
Este bloque es opcional y se ejecuta cuando no se genera una excepción dentro del try
'''
try:
	x = int(input("Dame un número"))
	resultado = 5/x
except:
	print("Ocurrio un error")
else:
	print("El resultado de la operación es: ",resultado)

#Cláusula finally
'''
Esta se ejecuta si no hay error en try 
si hay un bloque ELSE también se ejecuta, después del bloque else
si ocurre un error manejado por except se ejecuta 
si ocurre un error que no es manejado por except también se ejecuta
Y como podrás ver siempre se ejecuta, esto es útil para liberar recursos externos
sin importar si el suo del recurso fue exitoso o no.
(cerrar archivos o conexiones de red (DB))
'''
try:
	x = int(input("Dame un número"))
	resultado = 5/x
except:
	print("Ocurrio un error")
else:
	print("El resultado de la operación es: ",resultado)
finally:
	del(x)
	del(resultado)
	print("Liberando espacio ocupado por las variables.")

#Levantando excepciones RAISE
'''
También podemos levantar excepciones usando la sentencia raise
debemos indicar el tipo de error y un mensaje opcional 
raise ZeroDivisionError
raise ZeroDivisionError("!Dividiste entre cero¡")
Esto cortara el flujo del programa
'''
print("Hola antes de la excepcion")
raise ZeroDivisionError("!Dividiste entre cero¡")
print("Hola después de la excepción")

#Podemos usar raise sin parámetros dentro de un except para re-lanzar la excepción ocurrida
try:
	x = int(input("Dame un número"))
	resultado = 5/x
except:
	print("Ocurrio un error")
	raise 
