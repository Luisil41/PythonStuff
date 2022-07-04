class Animal():
    especie = ''
    altura = ''
    peso = ''

    def __init__(self, especie, altura, peso):
        self.especie = especie
        self.altura = altura
        self.peso = peso

    def comer(self):
        print('Estoy comiendo')

    def cazar(self):
        print('Voy a cazar')

    def dormir(self):
        print('Voy a dormir')


class Leon(Animal):
    def __init__(self, altura, peso):
        super().__init__('Leon', altura, peso)


class Mascota():
    nombre = ''
    amo = ''

    def __init__(self, nombre, amo):
        self.nombre = nombre
        self.amo = amo

    def sentarse(self):
        print('Estoy sentado')

    def dar_pata(self):
        print('Te doy la pata')


class Perro(Animal, Mascota):
    def __init__(self, nombre, amo, altura, peso):
        Animal.__init__(self, 'Perro', altura, peso)
        Mascota.__init__(self, nombre, amo)


luis = Perro('Blas', 'Luis', 0.4, 10)
luis.cazar()
luis.dormir()
luis.sentarse()
print(luis.nombre)
print(luis.especie)
