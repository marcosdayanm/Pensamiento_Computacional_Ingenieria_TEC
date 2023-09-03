def del_dup(l):
    newl = []
    for i in l:
        if i not in newl:
            newl.append(i)
    return newl

def input_list(numelem):
    lista = []
    for i in range(numelem):
        num = int(input("Type a number: "))
        lista.append(num)
    return lista

numelem = int(input("Choose the # of elements you want to introduce: "))  

call1 = input_list(numelem)
call2 = del_dup(call1)

print(call2)
    