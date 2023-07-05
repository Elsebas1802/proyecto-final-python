value = 1
while value <= 5:
    print(value)
    value += 1
    print(" Programa 28. Programa que evalua Calificaciones")
    evaluacion = float(input("escriba la nota:"))
    if evaluacion >= 90 and evaluacion <= 100:
        print(" su evaluacion es A")
    elif evaluacion >= 80 and evaluacion <= 89:
        print(" su evaluacion es B")
    elif evaluacion >= 70 and evaluacion <= 79:
        print(" su evaluacion es C")
    elif evaluacion >= 60 and evaluacion <= 69:
        print(" su evaluacion es D")
    else:
        print(" su evaluacion es F")
    print(" /n Final del programa")