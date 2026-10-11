#heladeria

Precio_helado = 1.90

total = 0
otro_pedido = "si"

while otro_pedido == "si":
    print("\n ¡Bienvenido a la heladería de Andresco!")
    print(f"Nuestro helado sin toppings cuesta ${Precio_helado:.2f}.")

    quiere_topping= input("¿Desea agregar un topping? (si/no): ").lower().replace("í","i")

    if quiere_topping == "si":
        print("\n ---Menú de toppings---")
        print("frutas   $0.50")
        print("granola  $1.50")
        print("oreo     $1.00")
        print("brownie  $0.75")
        topping= input("¿Cuál topping desea agregar?: ").lower()

        if topping == "frutas":
            precio= 0.50
        elif topping == "granola":
            precio= 1.50
        elif topping == "oreo":
            precio= 1.00
        elif topping == "brownie":
            precio= 0.75
        else: 
            print("!Lo sentimos, no tenemos ese topping!. "
                  "Te serviremos tu helado sin topping.")
            precio= 0
    else:
        precio= 0
    total= total+ Precio_helado + precio
    print(f"Pedido agregado. Llevas un total de ${total:.2f}.")

    otro_pedido= input("\n¿Desea hacer otro pedido? (si/no): ").lower().replace("í","i")

print(f"\n¡Gracias por confiar en la heladería de Andresco! El total a pagar es: ${total:.2f}.")

