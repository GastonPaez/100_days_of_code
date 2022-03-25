year = int(input("Type a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is leap.")
        else:
            print("The year is not leap.")
    else:
        print("The year is leap.")
else:
    print("The year is not leap.")
