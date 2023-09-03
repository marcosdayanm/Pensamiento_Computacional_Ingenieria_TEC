age=int(input("Enter your age: "))
id=input("Did you brought your ID? (answer yes/no): ")

if age>=18 and id=="yes":
    print("You can enter to the club")
elif age>=18 and id=="no":
    print("Just bring your ID and you can enter to the club")
else:
    print("Go away kiddo")