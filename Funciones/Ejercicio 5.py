#Numero mas grande

def maximo_recursivo (numeros):
    if len (numeros)==1:
        return numeros [0]

    resto = maximo_recursivo(numeros[1:])

    if numeros [0]>resto:
        return numeros[0]
    else:
        return resto 


print (maximo_recursivo([4, 5, 7, 12, 65]))