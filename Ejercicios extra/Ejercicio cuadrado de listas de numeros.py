lista = []

num = int(input("Teclee el numero de sub-listas que va a ser también el numero de elementos por cada lista: "))

def matriz(num):
    squared = num**2
    count = 0
    x = []
    for i in range(squared):
        print(count,end=" ")
        x.append(count)
        if len(x) == num:
            count +=1
            print()
            x = []

call = matriz(num)

