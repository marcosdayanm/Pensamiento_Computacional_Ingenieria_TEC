
import random

def game(num):
    pregunta = input("Hazme una pregunta: ")
    if num ==1:
        return "Chancla"
    elif num==2:
        return "Nel papi"
    elif num==3:
        return "Simon carnal"
    elif num==4:
        return "Concentrate y pregunta otravez"
    elif num==5:
        return "No creo"
    elif num==6:
        return "Pregúntale a tu hermana"
    elif num==7:
        return "¿Porqué preguntas esas mamadas?"
    elif num==8:
        return "Ya verás"


numero=random.randint(1,8)
function = game(numero)
print(function)


