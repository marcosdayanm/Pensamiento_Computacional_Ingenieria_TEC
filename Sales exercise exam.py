

sales = [["  ",2020,2021],
         ["Q1",1164,1000],
         ["Q2",2341,9050],
         ["Q3",1233,3564],
         ["Q4",6587,6500]]

def printsales():
    for w in sales:
        print()
        for z in w:
            print(z, end = "  ")

while True:
    printsales()
    print("\n\n1. Update all sales data")
    print("2. Update one item")
    print("3. Show table\n")
    
    
    accion = int(input("What action do you want to select? Choose between 1,2 or 3: "))
    if accion == 1:
        # Changing the years
        a1 = int(input("Type the first year you want to change instead of 2020: "))
        a2 = int(input("Type the second year you want to change instead of 2021: "))
        sales[0][1] = a1
        sales[0][2] = a2
        
        # Modifying the sales of first year
        q1_2020 = int(input("Type the sales of the Q1 of your first year: "))
        q2_2020 = int(input("Type the sales of the Q2 of your first year: "))
        q3_2020 = int(input("Type the sales of the Q3 of your first year: "))
        q4_2020 = int(input("Type the sales of the Q4 of your first year: "))
        sales[1][1] = q1_2020
        sales[2][1] = q2_2020
        sales[3][1] = q3_2020
        sales[4][1] = q4_2020
        
        # Modifying the sales of second year
        q1_2021 = int(input("Type the sales of the Q1 of your second year: "))
        q2_2021 = int(input("Type the sales of the Q2 of your second year: "))
        q3_2021 = int(input("Type the sales of the Q3 of your second year: "))
        q4_2021 = int(input("Type the sales of the Q4 of your second year: "))
        sales[1][2] = q1_2021
        sales[2][2] = q2_2021
        sales[3][2] = q3_2021
        sales[4][2] = q4_2021
        
        print("Information succesfully uploaded, this is your new table: \n")
        printsales()
    
    elif accion == 2:
        printsales()
        what = int(input("What item would you like to update? "))
        new = int(input("What will be your new item? "))
        if what == sales[0][1]:
            sales[0][1] = new
        elif what == sales[1][1]:
            sales[1][1] = new
        elif what == sales[2][1]:
            sales[2][1] = new
        elif what == sales[3][1]:
            sales[3][1] = new
        elif what == sales[4][1]:
            sales[4][1] = new
        elif what == sales[0][2]:
            sales[0][2] = new
        elif what == sales[1][2]:
            sales[1][2] = new
        elif what == sales[2][2]:
            sales[2][2] = new
        elif what == sales[3][2]:
            sales[3][2] = new
        elif what == sales[4][2]:
            sales[4][2] = new
        
        print("Information succesfully uploaded, this is your new table: \n")
        printsales()
            
            
    elif accion == 3:
        print("This is the table")
        printsales()
    
    else:
        print("invalid, choose between 1,2 or 3")
        continue
    
    
        
    break
