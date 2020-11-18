lista = [7, 9, 5, 1, 2, 6, 8, 0, 3, 4]
listaOrdenada = [250, 521, 55, 55, 555, 555, 555, 555, 555, 555]

while 1:
    ordenar = int(input("¿Como desea ordenar? \n 1 de menor a mayor \n 2 de mayor a menor \n : "))
    if ordenar == 1:
        for f in range (10):
            X = lista[f]
            y = 0
            for i in range (10):
                if X > lista[i]:
                    pass
                elif X <= lista[i]:
                    y = X
                    X = lista[i]
                    #print("X viene con: ", X)
                    lista[f] = X
                    lista[i] = y

        for i in range (10):
            #print(listaOrdenada[i])
            print(lista[i])
    elif ordenar == 2:
        for f in range (10):
            X = lista[f]
            y = 0
            for i in range (10):
                if X < lista[i]:
                    pass
                elif X >= lista[i]:
                    y = X
                    X = lista[i]
                    #print("X viene con: ", X)
                    lista[f] = X
                    lista[i] = y

        for i in range (10):
            #print(listaOrdenada[i])
            print(lista[i])
    else:
        print("Ingrese un numero valido")


        




        

