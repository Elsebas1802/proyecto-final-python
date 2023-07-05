#programa4
def programa4():
    print ("programa4")
    print ("Programa que calcula el area de un triangulo \n")
base = input("Escriba la base: ")
altura = input("Escriba la altura: ")
hipotenusa = input("Escriba la hipotenusa: ")

b = float(base)
a = float(altura)

area = (b * a)/2

DR = round (area, 2)

print("Imprimir: ", DR)