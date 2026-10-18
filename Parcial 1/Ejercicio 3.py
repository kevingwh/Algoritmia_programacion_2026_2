##maquina de arroz

limite = 40
capacidad = 10
hay_bolsa = True
capacidad_tolva = 100
arroz_tolva = 100
consumo_bolsa = 10

caja = []
cajas = 0
bolsas_total = 0
ciclos = 0

print("=== Máquina empacadora de arroz encendida ===\n")

while True:
    ciclos = ciclos + 1
    if ciclos > limite:
        print("\n=== Fin de la demostración ===")
        break

    hay_bolsa = True
    if ciclos % 6 == 0:
        hay_bolsa = False

    if not hay_bolsa:
        print("Esperando bolsa...")
        continue

    if arroz_tolva < consumo_bolsa:
        print("Tolva vacía: se rellena la tolva...")
        arroz_tolva = capacidad_tolva

    print("Vaciando arroz en la bolsa...")
    arroz_tolva = arroz_tolva - consumo_bolsa
    print("Arroz restante en la tolva", arroz_tolva)
    print("Sellando la bolsa...")

    bolsas_total = bolsas_total + 1
    caja.append("Bolsa " + str(bolsas_total))
    print("Bolsa empacada (" + str(len(caja)) + " de " + str(capacidad) + ")")

    
    if len(caja) == capacidad:
        cajas = cajas + 1
        print(">>> CAJA LLENA: caja #" + str(cajas) + " despachada <<<")
        caja = []

print("Bolsas empacadas en total:", bolsas_total)
print("Cajas despachadas:", cajas)
print("Bolsas en la caja actual:", len(caja))