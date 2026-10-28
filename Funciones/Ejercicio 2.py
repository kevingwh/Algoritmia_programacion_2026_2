#Funcion que recorre una lista

def pares_cuadrados(numeros):
    if numeros == []:
        return []
    resto = pares_cuadrados(numeros[1:])

    if numeros [0] % 2==0:
        return [numeros [0]**2] + resto
    else:
        return resto


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(pares_cuadrados(numeros))

