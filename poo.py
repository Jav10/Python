#Programación Orientada a Objetos
#Autor: Javier Arturo Hernández Sosa
#Fecha: 15/Sep/2017
#Descripcion: Curso Python FES Acatlán

#Declaración de clases
class Empresa:
	pass
	
#Atributos de clases
class Empresa:
	nombre = None
	apellido = None

#Crear objeto
empleado = Empresa()

#Mostrar atributos
empleado.nombre = "Max"
print(empleado.nombre)	

#Métodos de clase	
class Empresa:
	def salario(self):
		print("Salario: 10000000.")

empleado = Empresa()
empleado.salario()

class Empresa:
	nombre = None
	def setNombre(self, nombre=None):
		self.nombre = nombre	
#Método __init__ (Inicializa un Objeto) 
class Empresa:
	def __init__(self,nombre=None,apellido=None):
		self.nombre = nombre
		self.apellido = apellido
		
#Todo Junto
class Empresa:
	def __init__(self,nombre=None,apellido=None):
		self.nombre = nombre
		self.apellido = apellido
		
	def setNombre(self, nombre=None):
		self.nombre = nombre	

		
#Métodos especiales init y del (constructor y destructor)
class Empresa:
	def __init__(self):
		print("Creando el objeto",self,"Llamada a constructor")
	def __del__(self):
		print("Destruyendo el objeto",self,"Llamada al destructor")

empleado = Empresa()
del empleado
		
#Método str
class Empresa:
	def __str__(self):
		return "Regresando cadena: Arturo Hernández Curso Python FES Acatlán"

empleado = Empresa()		
str(5)
str(empleado)
		
#Método length
class Empresa:
	def __init__(self):
		self.jornada = 9
	def __len__(self):
		return self.jornada

empleado = Empresa()		
print("el empleado lleva ",len(empleado),"años trabajando aquí")		

#Objetos de objetos
class Empleado:
	#Constructor
	def __init__(self,nombre,apellido,clave):
		self.nombre = nombre
		self.apellido = apellido
		self.clave = clave
	
	def __str__(self):
		return '{0} {1} con clave: {2}'.format(self.nombre,self.apellido,self.clave)
		
class Empresa:
	def __init__(self, empleados=[]):
		self.empleados = empleados
	def insertar(self, objeto):
		self.empleados.append(objeto)
	def ver(self):
		for i in self.empleados:
			print(i)
			
empleado1 = Empleado("arturo","hernandez",12345)
empleado2 = Empleado("javier","hernandez",54321)
e = Empresa([empleado1])
e.insertar(empleado2)
e.ver()	

#Herencia
class Animal(object):
	def __init__(self,nombre,genero,familia):
		self.nombre = nombre
		self.genero = genero
		self.familia = familia
	
	def __str__(self):
		return """\
		Nombre\t {}
		Genero\t {}
		Familia\t {}""".format(self.nombre,self.genero,self.familia)
		
class Gato(Animal):
	largo = None
	ancho = None
	
	def sonido(self):
		print("Miau")
		
	def __str__(self):
		return """\
		Nombre\t {}
		Genero\t {}
		Familia\t {}
		largo\t {}
		ancho\t {}""".format(self.nombre,self.genero,self.familia)	

g = Gato("Firus","Hembra","Felidae")
g.largo = ".8 metros"
g.ancho = ".15 metros"
g.nombre
g.ancho
g.sonido()	
str(g)
print(g)

#Otra forma
class Gato(Animal):
	def __init__(self,nombre,genero,familia,largo,ancho):
		Animal.__init__(self,nombre,genero,familia)
		self.largo = largo
		self.ancho = ancho

	def sonido(self):
		print("Miau")

	def __str__(self):
		return """\
		Nombre\t {}
		Genero\t {}
		Familia\t {}
		largo\t {}
		ancho\t {}""".format(self.nombre,self.genero,self.familia,self.largo,self.ancho)

g = Gato("Firus","Hembra","Felidae",".8 metros",".15 metros")
		
#Polimorfismo
class Aguila:
	def avanza(self):
		print("Vuela")

class Gusano:
	def avanza(self):
		print("Arrastrarse")

def mover(animal):
	animal.avanza()

a = Aguila()
g = Gusano()
a.avanza()
g.avanza()

mover(a)
mover(g)	

#Herencia Múltiple	
class A(object):
	def __init__(self,nombre,info):
		self.nombre = nombre
		self.info = info
		
	def metodo_A(self):
		print("Vengo de A")
		
class B(object):
	def __init__(self,clave):
		self.clave = clave
		
	def metodo_B(self):
		print("Vengo de B")
		
class C(A,B):
	def __init__(self,nombre, clave, info):
		A.__init__(self,nombre,info)
		B.__init__(self,clave)
		
	def metodo_C(self):
		print("Vengo de C")
		
herencia = C("Arturo",234,"Programador Python")
print(herencia.nombre)
print(herencia.info)
print(herencia.clave)
herencia.metodo_A()
herencia.metodo_B()
herencia.metodo_C()