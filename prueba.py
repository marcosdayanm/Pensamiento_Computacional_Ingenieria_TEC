display = [[" ",1,2,3,4,5,6],
            [1,"-","-","-","-","-","-"],
            [2,"-","-","-","-","-","-"],
            [3,"-","-","-","-","-","-"],
            [4,"-","-","-","-","-","-"],
            [5,"-","-","-","-","-","-"],
            [6,"-","-","-","-","-",""],]

contador = 0
for i in display:
            for j in i:
                if "-" == j:
                    contador += 1

print(contador)
