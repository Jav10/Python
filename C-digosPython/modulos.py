#Módulos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 24/Sep/2017
#Descripcion: Curso Python FES Acatlán

'''
import libreria
import libreria as lb
from libreria import funcion,variable
from libreria import funcion as fn
'''

import sys

print(sys.executable) #Muestra la ruta absoluta del ejecutable de python
print(sys.platform) #Muestra la plataforma de trabajo ejemplo: 'win32'
print(sys.version) #Version del interprete de python

import sys as s

print(s.executable) #Muestra la ruta absoluta del ejecutable de python
print(s.platform) #Muestra la plataforma de trabajo ejemplo: 'win32'
print(s.version) #Version del interprete de python

from sys import executable
from sys import platform
from sys import version

print(executable)
print(platform)
print(version)

from sys import executable as e
from sys import platform as p
from sys import version as v

print(e)
print(p)
print(v)