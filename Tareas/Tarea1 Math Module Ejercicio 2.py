# Math Module Homework Exercise 1 Marcos Dayan
import math
print("This program will ask you for the radius of a sphere and will calculate the Area and the Volume of it \n")

r=float(input("Insert the radius of the sphere: "))

a=4*math.pi*r**2
print("The area of the Sphere is: ", a)

v=(4*math.pi*r**3)/3
print("The volume of the Sphere is: ", v)
