print("Programa 19 que calcula la compra de 5 articulos /n")

precio1= input("precio del articulo1")
precio2 = input("precio del articulo2")
precio3 = input("precio del articulo3")
precio4 = input("precio del articulo4")
precio5 = input("precio del articulo5")

precio_del_articulo1 = float(precio1) 
precio_del_articulo2 = float(precio2) 
precio_del_articulo3 = float(precio3)
precio_del_articulo4 = float(precio4)
precio_del_articulo5 = float(precio5)

total_sin_impuesto = (precio_del_articulo1 + precio_del_articulo2 + precio_del_articulo3 + precio_del_articulo4 + precio_del_articulo5)
DR = round(total_sin_impuesto,2)
print("el total_sin_impuesto es ", DR)

total_con_impuesto = (precio_del_articulo1 + precio_del_articulo2 + precio_del_articulo3 + precio_del_articulo4 + precio_del_articulo5) + 7
DR = round(total_con_impuesto,2)
print("el total_con_impuesto es ", DR)

promedio_de_compra = (precio_del_articulo1 + precio_del_articulo2 + precio_del_articulo3 + precio_del_articulo4 + precio_del_articulo5) / 5
DR = round(promedio_de_compra,2)
print("el promedio_de_compra es ", DR)


