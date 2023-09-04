import random

nums = random.randint(1, 100)
intn = 0
adv = False

print("Adivina el numero")

while not adv:
    intn += 1
    print(f"Intento {intn} :")
    numu = int(input())

    if numu < nums:
        print(f"El número es mayor que {numu}")
    elif numu > nums:
        print(f"El número es menor que {numu}")
    else:
        adv = True
        print(f"Correcto. Adivinaste en {intn} intentos!")
