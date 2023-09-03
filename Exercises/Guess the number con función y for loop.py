import random

def guess():
    for i in range(2):
        x = random.randint(1,5)
        num = int(input("Guess a number between 1 and 5, you have 2 chances: "))
        if num == x:
            print("You have guessed the number")
            print("+1 point")
            return 1
        else:
            print("You didn't guessed the number")
            if i>=1:
                return 0
            else:
                continue

r = int(input("How many rounds would you like to play? "))

p1 = 0
p2 = 0

for i in range(r):
   print(f"\nPlayer 1 round {i+1}:")
   p1 += guess()
   print(f"\nPlayer 2 round {i+1}:")
   p2 += guess()
   
if p1>p2:
    print(f"Player 1 won with {p1} points!")
elif p2>p1:
    print(f"Player 2 won with {p2} points!")
else:
    print(f"Its a tie of {p1} points each one!")
   
