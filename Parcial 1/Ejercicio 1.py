##menú_comida rapida

total = 0
pedido = []

menu = {
    "hamburguesa tradicional": 14000,
    "papas a la francesa": 5000,
    "perro caliente": 10500,
    "pizza personal": 12500,
    "malteada de chocolate": 8000,
    "gaseosa": 4000
}

print ("====MENÙ DE COMIDA RÁPIDA====")
for plato, precio in menu.items():
    print(plato, "-", precio)

while True:
    plato = input("\nIngrese el plato que desea: ").lower()
    while plato not in menu:
        print("¡Uy! Ese plato en este mismo instante no lo tenemos porque el preparador especial no está disponible. Por favor, elija otro plato del menú.")
        plato = input("Ingrese el plato que desea: ").lower()
    texto= input("Ingrese la cantidad que desea: ")
    while not texto.isdigit() or int(texto) <= 0:
        print ("¡Uy! No podemos procesar esas cantidades, que pena. Por favor, ingrese una cantidad válida.")
        texto = input("Ingrese la cantidad que desea: ")
    cantidad = int(texto)
    subtotal = menu[plato] * cantidad
    pedido.append((plato, cantidad, subtotal))
    total= total + subtotal

    respuesta = input("¿Desea hacer otro pedido? (s/n): ").lower()

    while respuesta != "s" and respuesta != "n":
        print ("¡Uy! No entendí su respuesta. Por favor, ingrese 's' para sí o 'n' para no.")
        respuesta = input("¿Desea hacer otro pedido? (s/n): ").lower()

    if respuesta == "n":
        break

print("\n===RESUMEN DE SU PEDIDO===")

for plato, cantidad, subtotal in pedido:
    print (plato, "-", cantidad, "-", subtotal)
print("TOTAL A PAGAR", total)


