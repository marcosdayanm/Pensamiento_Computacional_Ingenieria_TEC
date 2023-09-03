# Escribe un programa que lea la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos. El programa debe mostrar en la pantalla el precio correspondiente a cada artículo pedido, el programa debe repetirse mientras el usuario no teclee la clave X, cuando el usuario teclee la clave X el programa debe mostrar en la pantalla el total de la compra del cliente.

key = ""
price = 0
total = 0

while key != "X":
    key = input("Press one key letter to select a price (between A, B or C), press X to end: ")
    if key == "A":
        price = 120
    elif key == "B":
        price = 250
    elif key == "C":
        price = 360
    elif key == "X":
        continue
    else:
        price = 0
        print("Invalid key letter, please type another one, your account has still the previous keys inserted \n")
    total += price

print("The total of your purchase will be: $",total)