def adults(order):
    if order == 1:
        price = 200
    elif order == 2:
        price = 300
    elif order == 3:
        price = 250
    else:
        print("Invalid order")
        price = 0
    return price

def children(order):
    if order == 1:
        price = 150
    elif order == 2:
        price = 200
    elif order == 3:
        price = 175
    else:
        print("Invalid order")
        price = 0
    return price
    
def drinks(order):
    if order == 1:
        price = 20
    elif order == 2:
        price = 30
    elif order == 3:
        price = 15
    else:
        print("Invalid Order")
        price = 0
    return price

 
total = 0
ad = 0
cn = 0
dr = 0

while True:
    print("Welcome to Chilli's! \nChoose your menu:\n")
    print("1. Adults Menu \n2. Kids Menu \n3. Drinks Menu \n4. End Order \n")
    option = int(input("Choose an option from the menu: "))
    
    if option == 1:
        print("Adults Menu: \n\n1. Pasta - $200 \n2. Salmon - $350 \n3. Burger - $250 \n")
        order = int(input("Order your food: "))
        total += adults(order)
        ad += 1
    elif option == 2:
        print("Children Menu: \n\n1. Hot Dog - $150 \n2. Spaguetti - $200 \n3. Pizza - $175 \n")
        order = int(input("Order your food: "))
        total += children(order)
        cn += 1
    elif option == 3:
        print("Drinks Menu: \n\n1. Lemonade - $20 \n2. Coca Cola - $30 \n3. Water - $15 \n")
        order = int(input("Order your food: "))
        total += drinks(order)
        dr += 1
    elif option == 4:
        print(f"You have ordered {ad} adults meals, {cn} children meals and {dr} drinks\n")
        print(f"The total price is: ${total}\n")
        tip = input("Would you like to leave some tip? (yes/no): ")
        if tip == "yes":
            hm = int(input("How much percentage would you like to leave: "))
            totaltip = (hm/100+1)*total
            print(f"So the new total is: ${totaltip}\n")
        elif tip == "no":
            print("No problem\n")
            
        print("Thank you! Have a good meal")
        
        break
    else:
        print("Invalid Input")
