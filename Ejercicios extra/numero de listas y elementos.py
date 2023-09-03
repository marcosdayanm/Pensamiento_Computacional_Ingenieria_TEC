
nlistas = int(input("Inserte el numero de listas: "))
nelem = int(input("Inserte el numero de elementos en cada lista: "))
lista = []
listafinal = []
for i in range(1,nlistas*nelem+1):
    lista.append(i)
    if len(lista) == nelem:
        listafinal.append(lista)
        lista = []
        
print(listafinal)
        

