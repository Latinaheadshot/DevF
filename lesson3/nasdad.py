# Obtener un directorio usando python
# Python me regrese una lista d elos nombres de cotenido del carpeta genera una lista
# Saber como renombrar los archivos o transformarles el nombre
# El mismo nombre debe ser el mismo pero sin los numeros

# -*- coding: utf-8 -*-

import os
def lista_nombre():
    nombres_viejos = os.listdir("/Users/LaDulce/Desktop/dev.f Python")
    print(nombres_viejos)
  os.chdir("/Users/LaDulce/Desktop/dev.f Python")
    for letra in nombres_viejos:
        os.rename(letra, letra.translate("0123456789"))
        print(letra)
lista_nombre()
