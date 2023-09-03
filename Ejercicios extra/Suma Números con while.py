# Escribe un programa que sume los números enteros (positivos y negativos) que el usuario teclee y se detenga hasta que el usuario teclee un cero.
num = 1
result = 0
while True:
    num = float(input("Type a number and it wil be added to the previous result: "))
    if num != 0:
        result += num
        print("Now, the number is:",result, "\n")
    else:
        print("The final result of the sum is:", result)
        break