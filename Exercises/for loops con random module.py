# For loops
"""
import random

for i in range(2):
    print(random.randint(1,6))
"""

n = int(input("Insert and integer number: "))
suma = 0
for x in range(1,n):
    if n%x== 0:
        suma += x

if suma == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} isn't perfect")





