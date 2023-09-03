"""
#Función sin valor de entrada
def summation():
    print("This function will print the sum of two numbers")
    x = 5
    y = 3
    print("The result is:",x+y)
    
summation()
"""
"""
# Función con valor de entrada
def hello(n):
    print("Hello,",n)
    
name=input("Enter your name: ")
hello(name)
"""
"""
# Función con return
def summation(x,y,z):
    result=a+b+c
    return result

a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))

r = summation(a,b,c)
av =r/3
print("The average is:",av)
"""
"""
#Función que have un valor absoluto
def absvalue(num):
    if num>=0:
        return num
    else:
        return -num

n=int(input("Enter the number: "))
result=absvalue(n)
print(result)
"""
"""
# Función "al cubo"
def cube(n):
    return n**3

num = int(input("Enter the number: "))
result=cube(num)
print(result)
"""

#Función que intercambia valores 
def swap(x,y):
    print("This function will swap your values entered")
    temp=x
    x=y
    y=temp
    print("Swap swap swaaap")
    return x,y

a=int(input("Enter first number"))
b=int(input("Enter second number"))

numbers = swap(a,b)
print(numbers)




