#lista

lista =[2, 4, 3, 1, 6, 7, 5, 8, 9, 10]
original= lista.copy()
n= len(lista)

i = 0
while i < n -1:
    j = 0
    while j < n - 1- i:
        if lista[j] > lista[j + 1]:
            aux= lista[j]
            lista[j]= lista[j + 1]
            lista[j + 1]= aux
        j= j + 1
    i= i + 1
print ("Lista ordenada de menor a mayor: ", lista)

ordenada = sorted(original)

if lista == ordenada:
    print("¡Orden correcto!")
else:
    print("Hay un error.")