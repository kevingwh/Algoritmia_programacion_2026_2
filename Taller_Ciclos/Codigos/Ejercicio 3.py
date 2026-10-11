#longitud_palabras

palabra = input("Escriba una palabra: ")
n= len(palabra)

longitud=1
while longitud <= n:

    inicio =0
    while inicio + longitud <= n:
        print(palabra[inicio:inicio + longitud])
        inicio = inicio + 1

    longitud = longitud + 1