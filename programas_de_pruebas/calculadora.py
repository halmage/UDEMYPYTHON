nombre = input("Nombre: ")
venta = int(input("Venta: "))

operacion = venta * 13 / 100

redondeo = round(operacion, 2)

print(f"El {nombre} obtuvo un descuento de {redondeo}% en su venta.")
