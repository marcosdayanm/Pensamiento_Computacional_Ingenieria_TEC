
n = int(input("Insert one number bigger than 0: "))
if n<=0:
    print("Error, number must be bigger than 0")
else:
    for i in range(n):
        print(i+1,end=", ")
        
    for i in range(n-1,1,-1):
        print(i,end=", ")
    print(1)

    
