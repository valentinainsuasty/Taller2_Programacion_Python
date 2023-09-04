ttotal = 0

while True:
    ttramo = int(input("Duracion tramo: "))

    if ttramo == 0:
        break

    ttotal += ttramo

horas = ttotal // 60
mint = ttotal % 60

print(f"Tiempo total de viaje: {horas}:{mint} horas")
