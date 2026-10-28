def suma_recursiva (lista):
    if lista == []:
        return 0

    return lista [0]+ suma_recursiva(lista[1:])

numeros= [2, 4, 6, 8, 10]
print (suma_recursiva(numeros))
