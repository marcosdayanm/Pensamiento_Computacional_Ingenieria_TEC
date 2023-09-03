import math

def area_triangulo(b,h):
    area = b*h*.5
    return area

def area_circulo(r):
    area = math.pi*(r**2)
    return area

def area_cuadrado(l):
    area = l*l
    return area


que = input("A qué figura le quieres calcular el área? (triangulo, circulo, cuadrado): ")

if que == "triangulo":
    base = int(input("Ingresa la base del triángulo: "))
    altura = int(input("Ingresa la altura del triángulo: "))
    result = area_triangulo(base,altura)

elif que == "circulo":
    radio = int(input("Ingresa el radio de tu circulo: "))
    result = area_circulo(radio)

elif que == "cuadrado":
    lado = int(input("Ingresa el lado de tu cuadrado: "))
    result = area_cuadrado(lado)
else:
    print("Figura inválida o falta de otrografía, intente de nuevo")
    exit()

print(f"El área del {que} es {result}")
