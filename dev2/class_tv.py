class TV (obj):
    numero_de_tv = 0

    def __init__(self, nombre, tamano, tecnologia, precio):
        self.nombre = nombre
        self.tamano = tamano
        self.tecnologia = tecnologia
        self.precio = precio
        self.iva = precio * 16

    def nombre_de_tv(self):
        return "{}".format(self.nombre)

    def tamano_de_tv(self):
        return "{}".format(self.tamano)

    def tecnologia_de_tv(self):
        return "{}".format(self.botones)

    def precio_de_tv(self):
        return precio

    def precio_iva(self):
        return int(self.precio * 16)

samsung_tv = TV("Samsung","17 pulgadas", "HD", 10000)
toshiba_tv = TV("Toshiba", "18 pulgadas", "HD", 20000)
otra_tv = TV("Otra", "30 pulgadas", "HD", 30000)

print samsung_tv.__dict__