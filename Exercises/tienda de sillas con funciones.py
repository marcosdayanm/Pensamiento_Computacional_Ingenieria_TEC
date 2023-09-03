def price(chair, quantity):
    if chair == "basic":
        price = 700*quantity
    elif chair == "standard":
        price = 900*quantity
    elif chair == "deluxe":
        price = 1500*quantity
    else:
        print("Invalid chair type")
        price = 0
    return price

def frequent(p):
    discount = p*0.20
    print("The discount is: ",discount)
    total=p-discount
    print("The total price after discount is: ", total)
    
def normal(p):
    if p >=10000 and p<20000:
        discount = p*0.10
    elif p >=20000:
        discount = p*0.15
    else:
        discount = 0
    print("The discount is: ", discount)
    total = p-discount
    print("The total price after discount is: ", total)


chair = input("Type the chair type between basic, standard and deluxe: ")
costumer = input("Enter the customer type between normal and frequent: ")
quantity = int(input("How many chairs do you need? "))

price=price(chair, quantity)
print("The price before discount is: ", price)

if costumer == "normal":
    discount = normal(price)
elif costumer == "frequent":
    discount = frequent(price)
else:
    print("Invalid type of customer")


