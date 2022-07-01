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
