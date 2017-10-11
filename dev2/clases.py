# Instancia es objeto
# Metodo es una accion

class Empleado(object):
    # variable clase
    # Constante para todas las instancias
    monto_para_aumento = 1.04
    numero_de_empleados = 0

    # metodo init va a correr automaticamente cada que creamos una nueva instancia
    def __init__(self,nombre, apellido, salario):
        # self --> current instance
        self.nombre = nombre
        self.apellido = apellido
        self.correo = nombre + "." + apellido + "@company.com"
        self.salario = salario

        Empleado.numero_de_empleados += 1
    # no olvidar escribir self cada que definamos a un nuevo metado
    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)

    def obtener_salario(self):
        return self.salario

    def aplicar_aumento(self):
        self.salario = int(self.salario * self.monto_para_aumento)

class Utileria(object):


class Developer(Empleado,Utileria):
    monto_para_aumento = 1.10

    def __init__(self, nombre, apellido, salario, prog_lang):
        super(Developer,self).__init__(nombre,apellido,salario)
        self.prog_lang = prog_lang

empleado_1 = Empleado("Dulce","Ruvalcaba",10000)
developer_1 = Developer("Dulce","Ruvalcaba",1000s0, "Python")

print empleado_1





#print Empleado.numero_de_empleados

# Self es pasado automaticament por python, atributos son pasados en orden
#project_manager = Empleado("Dulce", "Lucero", 90000)
#QA = Empleado("Hugo", "Mecalco", 70000)

#print Empleado.numero_de_empleados
#print Empleado.__dict__
#print project_manager.__dict__
