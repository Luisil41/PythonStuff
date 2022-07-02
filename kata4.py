class Alumno():
    # Propiedades
    nombre = ""
    apellidos = ""
    __dni = ""
    __edad = 0
    asignaturas = []

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__dni = dni
        self.__edad = edad

    # Get / Set
    @property
    def dni(self):
        return self.__dni

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 100:
            self.edad = edad
        else:
            raise TypeError('Edad fuera del rango')

    # Metodos
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')

    def cumpleaños(self):
        self.__edad += 1

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


class Asignatura():
    #Propiedades
    __id = 0
    nombre = ""
    __nota = 0

    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    #Get / Set
    @property
    def id(self):
        return self.__id

    @property
    def nota(self):
        return self.__nota

    #Método
    def añadir_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.nota = nota


class Aula():
    __id = 0
    profesor = None
    alumnos = []
    asignaturas = []

    def __init__(self, alumnos, asignaturas):
       self.cargar_alumnos(alumnos)
       self.cargar_asignaturas(asignaturas)

       # Get / Set
    @property
    def id(self):
        return self.__id

    def mostrar(self):
        for alumno in self.alumnos:
            print(alumno.nombre)
        for asignatura in self.asignaturas:
            print(asignatura.nombre)

    def cargar_asignaturas(self, asignaturas):
        for nombre in asignaturas:
            nueva_asignatura = Asignatura(nombre)
            self.añadir_asignatura(nueva_asignatura)

    def cargar_alumnos(self, alumnos):
        for nombre in alumnos:
            nuevo_alumno = Alumno(nombre, '','', 18)
            self.añadir_alumno(nuevo_alumno)

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def quitar_asignatura(self, asignatura):
        self.asignaturas.remove(asignatura)

    def añadir_alumno(self, alumno):
        if alumno.edad >= 18:
            self.alumnos.append(alumno)

    def quitar_alumno(self, alumno):
        self.alumnos.remove(alumno)


luis = Alumno('Luis', 'Isarria', '4545454545S', 31)
print(luis.dni)
print(luis.edad)
luis.edad = 180
#print(luis.edad)
