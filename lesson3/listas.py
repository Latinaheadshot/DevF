# -*- coding: utf-8 -*-


#print (myList[2])
#print (myList[2:5])
#print (myList[5:])
#print (myList[:5])
#print (myList[:])

#myList = [1,2,3,4,5,6]
#def recorer_lista(myList):
    #m = 0
    #for i in range(len(myList)):
        #if m < myList[i]:
            #m = myList[i]
        #print(i,m)

#recorer_lista(myList)

#numero = int(input("Numero de palabras la lista:"))

#if numero < 1:
    #print("Imposible")
#else:
    #list = []
    #for i in range (numero):
        #print("Proporcione palabra"), str (i + 1) + ": "
        #palabra = input()

    #print ("Lista creada es:", list)


#def lista(elementos=5):
    #respuesta = int(input("Lista de elementos?:"))
    #if respuesta < 5:
        #print ("Necesito una palabra:")

    #else:
        #print ("Otra cosa")

#lista()

#Crear un lugar donde guarde los numeros, pedir la IP que debe ser de 12 digitos
ip = []
ip = int(input("escribe tu IP: "))

#Validad que sean los 12 digitos y si faltan, imprimir que faltan
if ip < 12:
     print("Faltan numeros:")

#Validad que sea sólo números y remover el punto de los IPs





ip="000.000.000.000"

def ip_validator(to_validate):
    if len(to_validate) = 15
        print ("IP no valida")
        exit(0)
    splited_ip = to_validate.split('.')