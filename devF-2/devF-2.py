#Encoding
# -*- coding: utf-8 -*-


# Funciones
#def saludar (nombre, mensaje=('Hola')):
 #   print (mensaje, nombre)

#saludar("Hugo")
#saludar ("hola", "sup")
#saludar (mensaje="Buen dia", nombre="hugo")

#Funciones Recursivas
#def play(intento=1):
    #respuesta =  input("De que color es una naranja?")
    #if respuesta != "naranja":
        #if intento < 3:
            #print ("\nFallaste! Intentalo de nuevo")
            #intento += 1
            #play (intento) # Llamada recursiva
        #else:
            #print ("\nPerdiste")
    #else:
        #print ("\nGanaste")
#play()

#Asignacio multiple
#def printing ():
    #a,b,c = "string", 15, True
    #mi_tupla = ('Hola mundo', 2014)
    #texto, anio = mi_tupla
    #print (str(a))
    #print (str(b))
    #print (str(c))
    #print (str(texto))
    #print (str(anio))

#printing()

#While
#def the_while():
    #while True:
        #nombre = input("Indique su nombre:")
        #if nombre:
            #print (nombre)
            #break
#the_while()

#for
#def the_for():
    #mi_lista = ["La", "Dulce", "Ruvalcaba"]
    #for nombre in mi_lista:
        #print (nombre)
    #mi_tupla = ["Los", "vengadores", "y ya"]
    #for color in mi_tupla:
        #print (color)
    #for anio in range (2001,2013):
        #print("Informe del Año", str(anio))
#the_for()

#Maquina de Dulces
#2.5 1.4 4 y 1.2

#def iniciar():
    #money = input("Cuanto dinero tienes?")
    #imprimirProductos(money)

#def imprimirProuctos(money):
    #print "\nLos dulces son:"
    #dulces = ["Panditas", "Chocoretas", "Mazapan", "Chipis"]

#productos()


#def iniciar():
    #dulce = input("Elija letra:")
    #if dulce=="a":
        #precioProducion=2.5
        #print ("Su vuelto", calcularVuelto(monto,precioProducto))
    #elif dulce=="b":
        #precioProducion=1.4
        #print ("Su vuelto", calcularVuelto(monto,precioProducto))
    #elif dulce=="c":
        #precioProducion=4
        #print ("Su vuelto", calcularVuelto(monto,precioProducto))
    #if dulce=="d":
        #precioProducion=1.2
        #print ("Su vuelto", calcularVuelto(monto,precioProducto))

#def imprimirProductos():
    #print ("a) Panditas: 2.5, \nb) Chocoretas: 1.4 \nc) Mazapan: 4 \nd) Chipis: 1.2")

#def calcularVuelto():


#def tabla_uno():
    #for multiplicador in range (1,11):
        #print ("\n")
        #for i in range (1,11):
            #print("Tabla de multiplicar de", multiplicador, '*', i, '=', multiplicador*i)


#tabla_uno()



#Se necesitan 4 productos
#Precios de los produc

import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on" + time.ctime())
while break_count < total_breaks:
    time.sleep(2)
    webbrowser.open_new("https://www.youtube.com/watch?v=otHnkPD4sks")
    break_count = break_count + 1


