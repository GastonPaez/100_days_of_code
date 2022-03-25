print("Welcome to the tip Calculator.")
total = float(input("What was the total bill?"))
people = int(input("How many people to split the bill?"))
percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15?"))
if percentage == 10:
    calculate = (total / people) * 1.10
    print(f"Each person should pay: {round(calculate,2) }")
if percentage == 12:
    calculate = (total / people) * 1.12
    print(f"Each person should pay: {round(calculate,2)}")
if percentage == 15:
    calculate = (total / people) * 1.15
    print(f"Each person should pay: {round(calculate,2)}")
