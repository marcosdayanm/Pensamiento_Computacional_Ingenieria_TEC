x = [10,20,30,40,50,60]

y = [x[:2],
     x[2:4],
     x[4:]]

print(y)

for i in y:
    print()
    for j in i:
        print(j,end=" ")