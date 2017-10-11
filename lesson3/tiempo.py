#1 Pedir las horas
tiempo_horas = (int(input("Introduce tus horas:")))
#2 Validar que no sea mayor 24
if tiempo_horas > 24:
    print("No debe ser mayor a 24:")
#3 Pedir los minutos
tiempo_minutos = (int(input("Introduce tus minutos:")))
#4 Validar que no sea mayor a 60
if tiempo_minutos > 60:
    print("No debe ser mayor a 60")
#5 Si el tiempo es menor o igual 12 la hora se queda igual
if tiempo_horas <= 12:
#5 Imprimo el tiempo en horas, le concateno con un + el tiempo de minutos y le agrego el AM
    print(str(tiempo_horas) +":" + str(tiempo_minutos) + "AM")
#6 Si el tiempo que me dan es mayor a 12 entonces imprimo el tiempo en horas y le resto 12 para que me de el tiempo que es mayor a 13 y agregue lo mismo de paso 5
#el source es : http://es.wikihow.com/convertir-el-horario-de-24-horas-a-horario-am-y-pm
else:
    print(str(tiempo_horas - 12) +":" + str(tiempo_minutos) + "PM")








