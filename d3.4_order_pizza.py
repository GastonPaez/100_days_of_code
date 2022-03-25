print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L : ")
add_peperoni = input("Do you want Pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheesee? Y or N : ")

bill = 0
if size == "S":
    bill = 15
    if add_peperoni == "Y":
        bill += 2
    elif add_peperoni == "Y" and extra_cheese == "Y":
        bill += 2 + 1
    elif add_peperoni == "N" and extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill = 20
    if add_peperoni == "Y":
        bill += 3
    elif add_peperoni == "Y" and extra_cheese == "Y":
        bill += 3 + 1
    elif add_peperoni == "N" and extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    if add_peperoni == "Y":
        bill += 3
    elif add_peperoni == "Y" and extra_cheese == "Y":
        bill += 3 + 1
    elif add_peperoni == "N" and extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill} ")
