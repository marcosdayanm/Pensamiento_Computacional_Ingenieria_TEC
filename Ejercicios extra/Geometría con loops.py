letra = input("Escribe la letra: ")

def linea(letra):
    longi = int(input("Teclea la longitud que quieres que tenga la línea: "))
    linea = letra*longi
    return linea


def triangulo(letra):
    altura = int(input("Define la cantidad de filas que va a tener el triángulo: "))
    for i in range(1,altura+1):
        niveles = i*letra
        print(niveles)     
triangulo = triangulo(letra)
    
    
def revtri(letra):
    altura = int(input("Define la cantidad de filas que va a tener el triángulo: "))
    for i in range(altura, 0,-1):
        niveles = i*letra
        print(niveles)
inverso=revtri(letra)
