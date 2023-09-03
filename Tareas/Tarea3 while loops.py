# Este programa te va a pedir 2 números, el primero menor que el segundo y va a imprimir todos los intervalos que sean pares entre estos dos números, incluyendo los límites. El número 0 es considerado como par

print("This program will ask you for two numbers, the first one smaller than the second one, \nand will print every even number bewteen them, including them in case one of them or both are even. \nZero is considered as even number \n")
a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))
n = 0

if a>b:
    print("First number must be bigger than second one, try again \n")
elif a<b:
    while a<=b:
        if a%2 == 0:
            print (a)
            a += 2
        elif a%2 != 0:
            a += 1
else:
    print("First number must be bigger than second one, try again \n")