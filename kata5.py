class Usuario():
    nombre = ''
    apellidos = ''
    __dni = ''
    __edad = 0

    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

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


class Alumno(Usuario):
    asignaturas = []

    def __init__(self, nombre, apellidos, dni, edad):
        super().__init__(nombre, apellidos, dni, edad)

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

class Profesor(Usuario):
    especialidad = ''

    def __init__(self, nombre, apellidos, dni, edad):
        super().__init__(nombre, apellidos, dni, edad)