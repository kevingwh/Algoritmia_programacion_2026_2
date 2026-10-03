##clases

fecha = (input("Ingresar fecha (día, DD/MM): "))

datos = fecha.split(",")
dia_semana = datos[0]

fecha_numero = datos[1].split("/")
dia = int(fecha_numero[0])
mes = int(fecha_numero[1])

if dia > 31 or mes > 12:
    print("Se produjo un error")
elif dia_semana.lower()=="lunes":
    print ("Nivel inicial")

    examenes = input("¿Se tomaron exámenes? (si/no):")

    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de no aprobados: "))

        porcentaje = aprobados*100/(aprobados+no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")

elif dia_semana.lower()=="martes":
    print ("Nivel intermedio")

    examenes = input("¿Se tomaron exámenes? (si/no):")

    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de no aprobados: "))

        porcentaje = aprobados*100/(aprobados+no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")
elif dia_semana.lower()=="miércoles" or dia_semana.lower()=="miercoles":
    print ("Nivel avanzado")

    examenes = input("¿Se tomaron exámenes? (si/no):")

    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de no aprobados: "))

        porcentaje = aprobados*100/(aprobados+no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")
elif dia_semana.lower()=="jueves":
    print("Práctica hablada")

    asistencia = int(input("Ingrese la cantidad de alumnos presentes: "))

    if asistencia >50:
        print("Asistió la mayoria")
    else:
        print("No asistió la mayoria")
elif dia_semana.lower()=="viernes":
    print("Inglés para viajeros")

    if dia==1 and (mes==1 or mes==7):
        print("Comienzo de nuevo ciclo")

        alumnos = int(input("Ingrese la cantidad de alumnos: "))
        arancel = int(input("Ingrese el arancel: "))

        total = alumnos * arancel

        print("Ingreso total $", total)

else:
    print("Se produjo un error")
