pos = 0
neg = 0
while True:
    valor = int(input("Ingrese un valor entero: "))

    if valor == 0:
        break

    if valor > 0:
        pos += 1
    elif valor < 0:
        neg += 1

print("Valores positivos: " + "*" * pos)
print("Valores negativos: " + "*" * neg)
