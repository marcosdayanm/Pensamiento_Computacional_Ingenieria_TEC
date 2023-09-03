for i in range(2,101):
    num = 2
    while num<i:
        if i%num==0:
            break
        num+=1
    else:
        print(f"{i} is a prime number")
        