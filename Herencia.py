class Punto2D():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord2D(self):
        return [self.x, self.y]


class _Punto3D():
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coord2D(self):
        return [self.x, self.y]

    def coord3D(self):
        return [self.x, self.y, self.z]


class punto3D(Punto2D):
    z = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def coord3D(self):
        return [self.x, self.y, self.z]


p1 = Punto2D(1, 0)
p2 = _Punto3D(1, 0, 5)

print(p1.coord2D())
print(p2.coord2D())
print(p2.coord3D())