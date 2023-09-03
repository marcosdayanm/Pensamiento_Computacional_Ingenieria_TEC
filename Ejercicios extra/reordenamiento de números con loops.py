num = int(input("Type a positive or negatine integer number, with no more than 6 digits: "))
acomodacion = ""

if num >= 1000000:
    print("Number too big")
elif num <= -1000000:
    print("Number too small")
else:
    texto = str(num)
    medida = len(texto)
    if num>=0:
        for i in range(medida):
            acomodacion = texto[medida-1]
            print(acomodacion,end="")
            medida -=1
    elif num<0:
        print(texto[0],end="")
        for i in range(1,medida):
            acomodacion = texto[medida-1]
            print(acomodacion,end="")
            medida -=1
