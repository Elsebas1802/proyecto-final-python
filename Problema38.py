" Programa 38. Proyecto en Clases "

value = 1
while value <= 5:
    print(value)
    value += 1
    print("Programa que indica cual de los tres valores es mayor")
    
    a = float(input("escriba el valor 1: "))
    b = float(input("escriba el valor 2: "))
    c = float(input("escriba el valor 3: "))
    
    if a > b and a > c:
        print("el numero mayor es a = ", a)
    
    if b > a and b > c:
        print("el numero mayor es b = ", b)
        
    if c > a and c > b:
        print("el numero mayor es c = ", c)
    
    print(" Final del Programa")
        
