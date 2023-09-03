# Escribe un programa que lea 2 valores a y b y que muestre en la pantalla pares de números en donde el valor de a se incrementa de 2 en 2 y el valor de b se decrementa de 1 en 1 hasta llegar a 1. El ciclo se va a detener cuando b llegue a 1.

a = int(input("Insert first integer value: "))
b = int(input("Insert second integer value (it has to be greater than 1): "))

if b < 1:
    print("Invalid format, second value must be greater or equal than 1")
elif b >= 1:
    while b > 1:
        print(a,b)
        a += 2
        b -= 1
    else:
        print (a,b)