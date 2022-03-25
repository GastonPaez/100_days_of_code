import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me a everybody's names: ")
names = nameAsCSV.split(", ")
choice = random.randint(0, len(names))
print(f"{names[choice]} is going to buy the meal today! ")
