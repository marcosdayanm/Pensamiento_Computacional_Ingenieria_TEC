firstdisplay = [[" ",1,2,3,4,5,6],
                [1,"-","-","-","-","-","-"],
                [2,"-","-","-","-","-","-"],
                [3,"-","-","-","-","-","-"],
                [4,"-","-","-","-","-","-"],
                [5,"-","-","-","-","-","-"],
                [6,"-","-","-","-","-","-"],]
print("Player, select first the X axis and then the Y axis of your card")
for i in firstdisplay:
    print()
    for j in i:
        print(j, end=" ")

mainboard = [[" ",1,2,3,4,5,6],
             [1,"b","m","p","d","b","e"],
             [2,"r","k","a","d","i","j"],
             [3,"e","c","h","n","p","g"],
             [4,"n","f","o","c","m","q"],
             [5,"r","j","l","q","h","l"],
             [6,"f","a","g","k","i","o"],]

p1score = 0
p2score = 0

#maindisp = display()
    
#while (p1score + p2score) < 17:
p1roundx = int(input("\n\nEnter the X axis of your card: "))
p1roundy = int(input("Enter the Y axis of your card: "))
acess = mainboard[p1roundy][p1roundx]
print(acess)




