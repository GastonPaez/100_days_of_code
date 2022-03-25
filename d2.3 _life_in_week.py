age = int(input("What is your current age?"))

days = 365
weeks = 52
months = 12

time = 90 - age
total_days = days * time
total_weeks = weeks * time
total_months = months * time
print(
    f"You have {total_days} days, {total_weeks} weeks and {total_months} months left. ")
