height = input("Type you weight height: ")
weight = input("Type you weight: ")

bmi = int(weight) / float(height) ** 2
print(f"Your BMI is {bmi} ")
if bmi < 18.5:
    print("Your are Underweight")
elif bmi > 18.5 and bmi < 25:
    print("You have a normal weight")
elif bmi > 25 and bmi < 30:
    print("You are overweight")
elif bmi > 30 and bmi < 35:
    print("You are obese")
else:
    print("You have a clinically obese")
