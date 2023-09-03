# Programa hecho por Mauricio Shejtman y Marcos Dayan

import random

# Intro del juego
print("\n¡Hola! Bienvenidos a memoria. Este juego será jugado por 2 jugadores.\nEl jugador que acerte un par de cartas obtendrá un punto, y volverá a ir.\nAl abrirse todas las cartas el jugador que tenga la mayor puntuación ganará")

#Personalizacion de jugadores
P1=input("\nInserta el nombre del Jugador 1: ")
P2=input("\nInserta el nombre del Jugador 2: ")

# Selección de tema de cartas
while True:
    tema=input("\n¿Con qué tema te gustaría jugar? \n1. Letras mayúsculas (A-R) \n2. Letras minúsculas (a-r) \n3. Carácteres especiales (/,¿,^) \nEscoja un número del 1-3 para continuar: ")
    if tema == "1" or tema == "2" or tema == "3":
        break
    else:
        print("Se introdujo un valor inválido, escoja un tema con los números 1,2 o 3")

print(f"\n{P1}, {P2}, ¡Vamos a empezar!")
print() 

#Display
display = [[" ",1,2,3,4,5,6],
            [1,"-","-","-","-","-","-"],
            [2,"-","-","-","-","-","-"],
            [3,"-","-","-","-","-","-"],
            [4,"-","-","-","-","-","-"],
            [5,"-","-","-","-","-","-"],
            [6,"-","-","-","-","-","-"],]


def imprimetablero(l):
    for i in l: # 
            print()
            for j in i:
               print(j,end=" ")




# Función para hacer shuffle al tablero de valores
def mainboard():
    if tema == "1":
        l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
             "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",]
    elif tema == "2":
        l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",]
    elif tema == "3":
        l = ["+","*","´",":",";","|","°","^","}","[","¨","¿","!","#","&","%","=","@",
             "+","*","´",":",";","|","°","^","}","[","¨","¿","!","#","&","%","=","@",]
    
    random.shuffle(l)
    l.insert(0,1)
    l.insert(7,2)
    l.insert(14,3)
    l.insert(21,4)
    l.insert(28,5)
    l.insert(35,6)
    l.insert
    l=[l[:7],l[7:14],l[14:21],l[21:28],l[28:35],l[35:]]
    l.insert(0,[" ","1","2","3","4","5","6"])
    
    printmain = imprimetablero(l)
    return l

# Variable que almacena los valores del tablero
mainboard = mainboard()




# Función que corre un turno general que verifica si los inputs son correctos y dentro del rango
def turnos(turno):
    contador = 0
    while True:
        # Imprimir Tablero
        printdisplay = imprimetablero(display)
          
        # Turno 1
        while True:
            # Se introducen datos en string, para validar que sean integers, y en caso de que cualquier jugador tenga un error no se termine el juego
            x1s = input("\n\nIntroduce el eje X de tu primera carta: ")
            y1s = input("Introduce el eje Y de tu primera carta: ")
            # Se valida si los strings podrían ser convertidos a int o no
            if x1s.isdigit() != True or y1s.isdigit() != True:
                print("\nSe introdujo un valor no válido, deben ser números de entre 1 y 6, vuelve a intentar\n")
                continue
            # En caso de que si, se convierten a int, y ahora pasan por el filtro para ver si están dentro del rango adecuado
            else:
                x1 = int(x1s)
                y1 = int(y1s)
                if x1>6 or y1>6 or x1<1 or y1<1:
                    print("\nSe introdujo un valor no válido, deben ser números de entre 1 y 6, vuelve a intentar\n")
                    continue
                elif display[y1][x1] != "-":
                    print("\nSe introdujeron coordenadas de cartas que ya habian sido abiertas, vuelve a intentar\n")
                    continue
                else:
                    break
        # Se accede a la carta en el tablero con las cartas y se reemplaza en el tablero display 
        
        firstcard = mainboard[y1][x1]
        display[y1][x1] = firstcard
        
        # Se imprime nuevamente el tablero display con la primera carta
        printdisplay = imprimetablero(display)
    
        # Turno 2
        while True:
            # En el loop del segundo turno se realizan los mismos precesos que en el loop del primero, solo que guardando los datos en otras variables para así poder compararlas 
            x2s = input("\n\nIntroduce el eje X de tu segunda carta: ")
            y2s = input("Introduce el eje Y de tu segunda carta: ")
            if x2s.isdigit() != True or y2s.isdigit() != True:
                print("\nSe introdujo un valor no válido, deben ser números de entre 1 y 6, vuelve a intentar\n")
                continue
            else:
                x2 = int(x2s)
                y2 = int(y2s)
                if x2>6 or y2>6 or x2<1 or y2<1:
                    print("\nSe introdujo un valor no válido, deben ser números de entre 1 y 6, vuelve a intentar\n")
                    continue
                elif display[y2][x2] != "-":
                    print("\nSe introdujeron coordenadas de cartas que ya habian sido abiertas, vuelve a intentar\n")
                    continue
                else:
                    break
            
        secondcard = mainboard[y2][x2]
        display[y2][x2] = secondcard
            
        printdisplay = imprimetablero(display)
                
    # Verficar si se obtiene punto, y checar si el jugador vuelve a ir o se acaba su turno
        if firstcard == secondcard and (x1 != x2 or y1 != y2):   
            contador +=1
            if turno%2 != 0:
                if contador + score1 + score2 == 18:
                    return contador
                    break
                print(f"\n\n{P1} tiene una racha de {contador} punto(s), vuelve a ir")
                continue
            elif turno%2 == 0:
                if contador + score1 + score2 == 18:
                    return contador
                    break
                print(f"\n\n{P2} tiene una racha de {contador} punto(s), vuelve a ir")
                continue
        else:
            intentofallido = input("\n\n¡Rayos! No lograste abrir un par igual de cartas, presiona enter para continuar: ")
            display[y1][x1] = "-"
            display[y2][x2] = "-"
            break
    
    return contador
        


# Estructura general y orden de juego
turno = 1
juego = 0
score1 = 0
score2 = 0
while True:
    # Determinar a qué jugador le toca jugar
    if turno%2 != 0: # turno es non
        print(f"\n\nTurno de {P1}")
    elif turno%2 == 0: # turno es par
        print(f"\n\nTurno de {P2}")
    
    juego = turnos(turno)
        
    if turno%2!=0: # turno es non
        score1 += juego
    elif turno%2==0: # turno es par
        score2 += juego
        salir = input("\n\n¿Quieres terminar el juego con las puntuaciones actuales? (si/no): ")
        if salir.lower() == "si":
            break
    print(f"\n\n{P1} tiene {score1} puntos en total")
    print(f"{P2} tiene {score2} puntos en total")
    
    turno += 1
    if score1 + score2 == 18:
        break


# Declarar ganador final
if score1>score2:
    print(f"\n¡{P1} gana con {score1} puntos!")
elif score1<score2:
    print(f"\n¡{P2} gana con {score2} puntos!")
else:
    print(f"\nEs un empate, ambos jugadores obtuvieron {score1} puntos")


