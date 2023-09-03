# Escribe un programa que lea un valor n y que muestre en la pantalla n caracteres que alternan entre # y %.

a = "#"
b = "%"
n = 0
i = 0 

n = int(input("Type a int number to choose the number of symbols would you like to see: "))

while i < n:
    if i%2 == 0:
        print(a)
    elif i%2 != 0:
        print(b)
    i+=1


