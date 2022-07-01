class Alumno():
    # Propiedades
    nombre = ""
    apellidos = ""
    dnit = ""
    edad = 0
    nota = 0

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    # Metodos
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')

    def añadir_nota(self):
        self.edad += 1

    def cumplir_años(self, nota):
        if nota >= 0 and nota <= 10:
            self.nota = nota
