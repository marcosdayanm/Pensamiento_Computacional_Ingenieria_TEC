# Math Module Homework Exercise 1 Marcos Dayan
import math

print("This porgram will ask you for the length of the 3 sides of a triangle and will calculate the area of the triangle \n")

a=float(input("Digit the length of the first side: "))
b=float(input("Digit the length of the second side: "))
c=float(input("Digit the length of the third side: "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is: ",area)
