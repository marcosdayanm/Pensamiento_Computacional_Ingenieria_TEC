print("This program will ask you for the measures of three sides of a triangle,\nit will determine if your measures can make a triangle and if they can,\nthe program will tell you the type of triangle that you have\n")

s1=float(input("Enter the first side of the triangle: "))
s2=float(input("Enter the second side of the triangle: "))
s3=float(input("Enter the third side of the triangle: "))

if (s1,s2,s3>0) and s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
    if s1==s2==s3:
        print("You have an Equilateral triangle")
    elif s1==s2!=s3 or s2==s3!=s1 or s3==s1!=s2:
        print("You have an Isoceles triangle")
    else:
        print("You have a Scalene triangle")
else:
    print("Your measures can't make a triangle")

