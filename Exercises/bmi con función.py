def bmi(h,w):
    result = w/h**2
    return result

markh=float(input("Enter Mark's height on meteres: "))
markw=float(input("Enter Mark's weight on kilograms: "))
johnh=float(input("Enter John's height on meteres: "))
johnw=float(input("Enter John's weight on kilograms: "))

markbmi = bmi(markh,markw)
johnbmi = bmi(johnh,johnw)

print("Mark's BMI is: ",markbmi)
print("John's BMI is: ",johnbmi)

if markbmi > johnbmi:
    print("Mark's BMI is greater than John's BMI")
elif johnbmi > markbmi:
    print("John's BMI is greater than Mark's BMI")
else:
    print("Both BMI's are equal")