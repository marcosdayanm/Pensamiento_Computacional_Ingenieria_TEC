i = 1
result = 1
base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))

while i <= exp:
    result *= base
    i += 1

print(result)