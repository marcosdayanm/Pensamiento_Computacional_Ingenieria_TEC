import random

# Intro al juego
print("\nHola! Bienvenidos a memoria. Este juego será jugado por 2 jugadores, al finalizarse las cartas el jugador que tenga la mayor puntuación ganará")

# Puntuación de Players 1 y 2
score1 = 0
score2 = 0

# Función para hacer shuffle al tablero de valores
def mainboard():
    l =["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
        "A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"]
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
    return l

def turnos(turno):
    contador = 0
    while True:
        # Imprimir Tablero
        for i in display:
            print()
            for j in i:
               print(j,end=" ")
           
        # Turno 1
        x1 = int(input("\n\nIntroduce el eje X de tu primera carta: "))
        y1 = int(input("Introduce el eje Y de tu primera carta: "))
        firstcard = mainboard[y1][x1]
        # Reemplazar carta en display y en tablero main
        display[y1][x1] = firstcard
        mainboard[y1][x1] = "-"
        for i in display:
            print()
            for j in i:
               print(j,end=" ")
    
        # Turno 2
        x2 = int(input("\n\nIntroduce el eje X de tu segunda carta: "))
        y2 = int(input("Introduce el eje Y de tu segunda carta: "))
        secondcard = mainboard[y2][x2]
        # Reemplazar carta en display y en tablero main
        display[y2][x2] = secondcard
        mainboard[y2][x2] = "-"
        for i in display:
            print()
            for j in i:
               print(j,end=" ")
        
        # Verficar si se obtiene punto, y checar si el jugador vuelve a ir o se acaba su turno
        if firstcard == secondcard and (x1 != x2 or y1 != y2):
            contador +=1
            if turno%2 != 0:
                print(f"\n\nEl jugador 1 tiene una racha de {contador} punto(s), vuelve a ir")
            elif turno%2 == 0:
                print(f"\n\nEl jugador 2 tiene una racha de {contador} punto(s), vuelve a ir")
            continue
        else:
            mainboard[y1][x1] = firstcard
            mainboard[y2][x2] = secondcard
            display[y1][x1] = "-"
            display[y2][x2] = "-"
            break
    return contador
        

# Variable que almacena los valores del tablero
mainboard = mainboard()
print(mainboard)
#Display
display = [[" ",1,2,3,4,5,6],
            [1,"-","-","-","-","-","-"],
            [2,"-","-","-","-","-","-"],
            [3,"-","-","-","-","-","-"],
            [4,"-","-","-","-","-","-"],
            [5,"-","-","-","-","-","-"],
            [6,"-","-","-","-","-","-"],]

turno = 0
juego = 0
# Estructura y orden de juego
while True:
    if turno%2 >0 and turno != 0:
        score1 += juego
        print(f"\n\nJugador 1 tiene {score1} puntos en total")
    else:
        score2 += juego
        print(f"\n\nJugador 2 tiene {score2} puntos en total")
    turno += 1
    
    if turno>0 and turno%2 != 0:
        print("\n\nTurno del jugador 1")
    elif turno>0 and turno%2 == 0:
        print("\n\nTurno del jugador 2")
    
    juego = turnos(turno)
    
    totalscore = score1 + score2
    if totalscore == 17:
        break


# Declarar ganador final
if score1>score2:
    print("¡Jugador 1 gana con {score1} puntos!")
elif score1<score2:
    print("¡Jugador 2 gana con {score2} puntos!")
else:
    print("Es un empate, ambos jugadores obtuvieron {score1} puntos")
    
       
