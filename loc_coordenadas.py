import math

class Punto:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({} y {})".format(self.x, self.y)

    def cuadrante(self):

        if self.x > 0 and self.y > 0:
            print("{} pertence al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))


    def vector(self, p):

        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y -self.y))

    def distancia(self, p):

        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))

a = Punto(3, 6)
b = Punto(-1, 3)
c = Punto(4, -6)
d = Punto(-4, -2)
e = Punto(0, 0)

a.cuadrante()
b.cuadrante()
c.cuadrante()
d.cuadrante()
e.cuadrante()

a.vector(b)
b.vector(a)
c.vector(d)
d.vector(c)

a.distancia(b)
b.distancia(a)
c.distancia(d)
d.distancia(c)