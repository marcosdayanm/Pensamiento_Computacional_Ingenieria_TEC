"""
# while normal
n = int(input("Enter the number: "))
i = 1
suma = 0
r=0
while i<=n:
    suma += i
    i += 1
    print("Esta vuelta es la ", r, " y el número de esta vuelta es: ",suma)
    r+=1

#while con else
i=0
while i<=6:
    print(i)
    i+=1
else:
    print("end of the loop")
    

# annoying while loop
name = ""
while name != "Marcos":
    name = input("Please enter your name: ")
print("Hi,", name)


# while con break
i=1
while i<6:
    print(i)
    if i ==3:
        break
    i+=1

# Contraseña segura
password = ""
i = 0
while password != "1234":
    password = input("Enter your password: ")
    i += 1
    if i == 5:
        print("You have entered wrong the password 5 times, please try later")
        break
    elif password != "1234":
        print("Incorrect passoword \n")
    elif password == "1234":
        print("Correct password, you can enter")
""" 

# infinite loop
while True:
    name = input("Enter your name: ")
    if name != "Marcos":
        print("Incorrect name \n")
        continue
    
    password = input("Type your password: ")
    if password == "69":
        break
    elif password != "69":
        print("Incorrect password \n")
        
print("User and password correct, hi",name)

    