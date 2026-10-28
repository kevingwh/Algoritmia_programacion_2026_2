#Invertir cadena de texto

def invertir_cadena (texto):
    if texto == "":
        return ""
    
    return invertir_cadena(texto[1:])+texto[0]

print (invertir_cadena("martes"))