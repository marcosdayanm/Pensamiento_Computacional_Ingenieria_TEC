def draw(line):
    for i in range(line-1):
        print()
        for j in range(i+1):
            print("*", end="")
    for k in range(line,0,-1):
        print()
        for l in range(k):
            print("*", end="")
            
     

n = int(input("Enter the number of lines you want to print: "))

rectangle_t = draw(n)





