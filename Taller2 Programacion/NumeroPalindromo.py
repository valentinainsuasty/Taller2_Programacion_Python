def palindromo(num1):

    num1 = str(num1)

    num2 = num1[::-1]

    if num1 == num2:
        return True
    else:
        return False


num = int(input("Ingresa un numero: "))

if palindromo(num):
    print(f"{num} es un numero palindromo.")
else:
    print(f"{num} no es un numero palíndromo.")
