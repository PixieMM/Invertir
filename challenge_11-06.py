def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input ("Ingrese la palabra a invertir: ")

cadena_invertida = invertir_cadena(cadena)

print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)