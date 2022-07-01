class Alumno():
    # Propiedades
    nombre = ""
    apellidos = ""
    dnit = ""
    edad = 0
    asignaturas = []

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    # Metodos
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')

    def cumpleaños(self):
        self.edad += 1

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


class Asignatura():
    #Propiedades
    nombre = ""
    nota = 0

    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre


    #Método
    def añadir_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.nota = nota


class Aula():
    profesor = None
    alumnos = []
    asignaturas = []

    def __init__(self, alumnos, asignaturas):
       self.cargar_alumnos(alumnos)
       self.cargar_asignaturas(asignaturas)

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


alumnos = ['Pepe', 'Manolo', 'Ana']
asignaturas = ['Mates', 'Lengua', 'Sociales']

aula = Aula(alumnos, asignaturas)
aula.mostrar()