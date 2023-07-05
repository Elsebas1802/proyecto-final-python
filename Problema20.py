print("programa 20 que calcula el salario neto de un empleado /n")
SalarioBruto = int(input("ingresa su salario bruto: "))

SeguroSocial = SalarioBruto * 0.08
SeguroEducativo = SalarioBruto * 0.02
impuesto = SalarioBruto * 0.15
prestamo =  100


SalarioNeto = SalarioBruto - SeguroSocial - SeguroEducativo - impuesto - prestamo
print("la cantidad a pagar de su SeguroSocial es de ", SeguroSocial)
print("la cantidad a pagar de su SeguroEducativo es de ", SeguroEducativo)
print("la cantidad a pagar de su impuesto es ", impuesto)
print("la cantidad a pagar de su prestamo es de ", prestamo)


print("el SalarioNeto es de ", SalarioNeto)