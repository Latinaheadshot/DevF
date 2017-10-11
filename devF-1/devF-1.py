
# String + Enteros
say_hello = "Hello World"
myInt = 20
print(str(myInt) + say_hello )

#Boleanos + enteros + string
def other_sentense():
    bool = True
    name = "Dulce"
    age = 29
    pi = 3.14159


#print(name + 'is' + str(age) + ' yearls old.')

#print()

# Estructura de código, cuando terminas el código, el metodo se llama al final.
# Siempre se ponen dos puntos en lugar de { } y sólo dará el salto de renglón
# Después de un def se ponen dos puntos

#myAge = str(28) + " años"
#myBirthday = "Septiembre 25"

#def happyBirthDayDulce(myAge, myBirthday):
 #   print("Happy Birthday to you!")
  #  print("Happy Birthday to you!")
   # print("Happy Birthday, dear Dulce")
   # print("Happy Birthday, to yoooou!")
   # print(myAge)
   # print(myBirthday)


#happyBirthDayDulce(myAge, myBirthday)


# Una función dentro de otra función, las funciones SIEMPRE deben llevar ():

#def get_message():
   #return "hola Dulce"

#def happyBirthDayDulce():
    #print(get_message())
    #print("Happy Birthday to you!")
    #print(other_sentense())


#happyBirthDayDulce()



# If Else, al parecer el elif es como otro if
#def if_else_control():
   # numero1 = 4
   # numero2 = 5

    #if numero1 > numero2:
        #print (" {} mayor a {} ").format(numero1, numero2)
    #elif numero2 <= numero1:
        #print (" {} no es mayor a {} ").format(numero1, numero2)
    #else:
   #     print ("error")

#if_else_control()


#Esto es para medir string y saber si están más grande o nel
el_string = "este es un string que quiero medir"

#def string_size (string_size):
    #if string_size > 10:
        #print("es muy grande")
    #else:
        #print("Nice, está chido así")

#Este rollo es para contar y usar el while que sirve mientras no se cumpla X condición ejecuta X cosa
count = 5
while count <= 5:
    print(count, "is less than 5")
    count = + 1
    break
else:
    print(count, "is not less than 5")

count()


#for x in range (0,3)
 #   print ("We're on time %d" % (x))

#for x in my_range (1,10,2)
 #   print x

    #un programa que me haga recordar que cada 10 mins tomaré un descanso, importar libreria time, web ebroowers, ejecutar youtube,