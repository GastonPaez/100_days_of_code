print("Welcome to Love Calculator:!")
name1 = input("What is your name? ")
name2 = input("What is your crush name? ")

n1 = name1.lower()
n2 = name2.lower()
contador_decena = 0
contador_unidad = 0

for x in "true":
    if n1.count(x) > 0:
        contador_decena += n1.count(x)
    if n2.count(x) > 0:
        contador_decena += n2.count(x)
for x in "love":
    if n1.count(x) > 0:
        contador_unidad += n1.count(x)
    if n2.count(x) > 0:
        contador_unidad += n2.count(x)

pre_result = f"{contador_decena}{contador_unidad}"
result = int(pre_result)


if result < 10 or result > 90:
    print(f"Your score is {result}. You go together like coke and menthos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}. You are alright together.")
else:
    print(f"Your score is {result}.")
