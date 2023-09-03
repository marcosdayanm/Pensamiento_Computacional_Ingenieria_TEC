print("This program is a basic calculator, is going to ask you for two numbers and an operator and will give you the result \n")

num1 = float(input("Enter your first number: "))
op = input("Enter the operator (+,-,*,/): ")
num2 = float(input("Enter your first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
