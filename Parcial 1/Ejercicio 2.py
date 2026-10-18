total = 0
otro = "s"

while otro == "s":
    edad = input("\nIngrese la edad del cliente: ").strip()
    while not edad.isdigit():
        print("Error: la edad debe ser un número entero mayor o igual a 0.")
        edad = input("Ingrese la edad del cliente: ").strip()
    edad = int(edad)

    if edad < 5:
        precio = 0
    elif edad <= 18:
        precio = 5
    else:
        precio = 10

    total = total + precio
    print("El precio de la entrada es: $" + str(precio))

    otro = input("\n¿Hay otro cliente? (s/n): ").strip().lower()
    while otro != "s" and otro != "n":
        print("Error: escriba solo 's' o 'n'.")
        otro = input("¿Hay otro cliente? (s/n): ").strip().lower()

print("\nTotal a pagar por el grupo: $" + str(total))