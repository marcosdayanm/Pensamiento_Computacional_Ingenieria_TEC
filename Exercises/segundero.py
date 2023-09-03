def segundero (h,m,s):
    seconds=h*3600 + m*60 + s
    return seconds

hrs1= int(input("Insert the hours on the process 1: "))
mins1= int(input("Insert the minutes on the process 1: "))
seg1= int(input("Insert the seconds on the process 1: "))
total1 =segundero(hrs1,mins1,seg1)
print("your process one was:",total1,"seconds long \n")

hrs2= int(input("Insert the hours on the process 2: "))
mins2= int(input("Insert the minutes on the process 2: "))
seg2= int(input("Insert the seconds on the process 2: "))
total2 =segundero(hrs2,mins2,seg2)
print("your process two was:",total2,"seconds long \n")