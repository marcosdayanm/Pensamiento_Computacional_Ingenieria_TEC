n=int(input("Indica cuántos números fraccionarios quieres que sean sumados: "))

div = 1
for i in range(1,n+1,1):
    print(f"{i}/",end="")
    div += i
    if i<n:
        print(div,end=" + ")
    elif n==i:
        print(div,end="")
