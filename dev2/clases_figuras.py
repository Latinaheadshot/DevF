import math

class Figura(object):

    def area (self, area):
        return area
    #def talk(self):
        #raise NotImplementedError ("Subclass must implement abstract method")

class Triangulo(Figura):
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def area(self):
        return (self.b * self.a) / 2

    def talk(self):
        print "te falta el metodo"

class Cuadrado(Figura):
    def __init__(self, b):
        self.b = b
    def area(self):
        return  self.b * 2

class Circulo(Figura): #pi * radio al cuadrado
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.sqrt(3.1416 * self.r)

class Otro(object):
    def __init__(self, name):
        self.name = name








triangulo = Triangulo(3,3)
print triangulo.area()
cuadrado = Cuadrado(4)
print cuadrado.area()
circulo = Circulo(34)
print circulo.area()

