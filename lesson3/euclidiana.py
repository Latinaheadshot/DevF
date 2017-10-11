# -*- coding: utf-8 -*-
#1 Paso 1 pido los datos X
x1 = (int(input("¿Cuál es tu distancia 1?")))
x2 = (int(input("¿Cuál es tu distancia 2?")))
#2 Paso pido los datos de Y
y1 = (int(input("¿Cuál es tu vector 1?")))
y2 = (int(input("¿Cuál es tu vector 2?")))
#3 Resto los datos de X
resta_X = x2-x1
#4 Resto los datos de Y
resta_Y = y2-y1
#5 Multiplicacion de paso restas de X
multiplicacion_X = resta_X * resta_X
#6 Multiplicacion de paso restas de y
multiplicacion_Y = resta_Y * resta_Y
#7 Multiplicacion de
suma_Multiplicaciones = multiplicacion_X + multiplicacion_Y
#8 Sacar raiz cuadrada
raiz_Cuadrada_Resultados = (suma_Multiplicaciones)** (.5)
# Imprimir resultado
print (raiz_Cuadrada_Resultados)




