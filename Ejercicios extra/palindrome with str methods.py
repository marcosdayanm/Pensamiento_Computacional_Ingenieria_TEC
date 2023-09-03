
word = input("Insert a word and the program will tell you if it is a palindrome or not: ")

def palindrome(w):
    wlower = w.lower()
    print(wlower)
    wnospace = wlower.replace(" ","")
    print(wnospace)
    wreverse = "".join(reversed(wnospace))
    if wnospace == wreverse:
        return f"The word {word} is a palindrome"
    else:
        return f"The word {word} is not a palindrome"
    
call1 = palindrome(word)
print(call1)

