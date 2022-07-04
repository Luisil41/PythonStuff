class Persona():
    nombre = ''
    edad = ''

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add(self, persona):
        pareja = Pareja(self, persona)
        return pareja


class Pareja():
    relacion = []

    def __init__(self, persona1, persona2):
        self.relacion.append(persona1)
        self.relacion.append(persona2)

    def mostrar(self):
        for persona in self.relacion:
            print(persona.nombre)


class Familia():
    miembros = []

    def añadir_miembro(self, persona):
        self.miembros.append(persona)


persona1 = Persona('Luis', 30)
persona2 = Persona('Marta', 31)
persona3 = Persona('Jorge', 22)

pareja = persona1 + persona2
pareja.mostrar()