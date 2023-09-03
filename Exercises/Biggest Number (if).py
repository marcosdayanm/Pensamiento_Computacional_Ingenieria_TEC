print("This program will ask you for three different numbers and is going to find the biggest one \n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print(num1,"is the biggest number")
elif num2 > num1 and num2 > num3:
    print(num2,"is the biggest number")
else:
    print(num3,"is the biggest number")
