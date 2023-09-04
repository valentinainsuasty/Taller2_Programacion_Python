cdatos = int(input("¿Cuantos valores ingresara?: "))

datos = []
for i in range(cdatos):
    dato = float(input(f"Ingrese el dato {i + 1}: "))
    datos.append(dato)

vmin = min(datos)
vmax = max(datos)

rango = vmax - vmin

print(f"El rango de los datos ingresados es: {rango}")
