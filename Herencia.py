class Punto2D():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord2D(self):
        return [self.x, self.y]

class Color():
    rojo = 'ROJO'
    negro = 'NEGRO'
    verde = 'VERDE'
    actual = ''

    def __init__(self, color):
        self.actual = color

class Punto3D(Punto2D, Color):
    z = 0

    def __init__(self, x, y, z):
        Punto2D.__init__(self,x, y)
        Color.__init__(self,'NEGRO')
        self.z = z

    def coord3D(self):
        return [self.x, self.y, self.z, self.actual]


p1 = Punto2D(1, 0)
p2 = Punto3D(1, 1, 5)


print(p1.coord2D())
print(p2.coord2D())
print(p2.coord3D())

