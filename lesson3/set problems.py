def sumas():
    uno = {1,2,3,4,5}
    dos = {4,5,6,7,8}
    print("Esta es la union", uno | dos)
    print("Esta es la intersección", uno & dos)
    inter = uno.union(dos)
    print(inter)
sumas()