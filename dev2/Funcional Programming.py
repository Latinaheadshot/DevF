# -*- coding: utf-8 -*-

#def cube(x): return x*x*x
#print map(cube,range(1, 11))

def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, range(2,25))

#Cuando una variable esté en mayusculas, se vuelve una constante por lo tanto no se puede cambiar
#Cuando una variable esté en minuscula, se puede cambiar