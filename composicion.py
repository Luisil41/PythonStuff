class Jugador():
    #Propiedades
    nombre = ""
    edad = 0
    rol = ""

    #Constructor
    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol

class Equipo():
    jugadores = []

    def mostrar_equipo(self):
        for jugador in self.jugadores:
            print(jugador.nombre)

    def añadir_jugador(self, jugador):
        self.jugadores.append(jugador)


j1 = Jugador('Pepe', 30, 'Media punta')
j2 = Jugador('Gerbasio', 33, 'Portero')
j3 = Jugador('Walter', 28, 'Defensa')

equipo = Equipo()
equipo.añadir_jugador(j1)
equipo.añadir_jugador(j2)
equipo.añadir_jugador(j3)

equipo.mostrar_equipo()
