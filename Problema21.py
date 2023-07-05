#Programa 21 - Calcular si una persona paga impuestos

salario = float(input("Escriba el Salario: "))

if salario < 3000:
    impuesto = salario * 1.07
    print("Esta Persona debe abonar impuestos", impuesto)
else:
    print("No Debe abonar impuestos")
    print("\n Fin del programa  ")