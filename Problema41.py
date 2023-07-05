"Programa 41. Programa que muestra si el valor es posotivo, negativo, cero"

def clasificar_numero(valor):
    if valor > 0:
        return "el valor es positivo"
    if valor < 0:
        return "el valor es negativo"
    else:
        return "el valor es cero"

valor = float(input("escribe un valor:"))
clasificacion = clasificar_numero(valor)

print(clasificacion)

print("Final del Programa")
