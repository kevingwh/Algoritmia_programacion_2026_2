##vocales

letra = input("Ingresar una letra: ").lower()

if len(letra) != 1:
    print("No se puede procesar el dato")
elif letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("Es vocal")
else:
    print("No es vocal")

