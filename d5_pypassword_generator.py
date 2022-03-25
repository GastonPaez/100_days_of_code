import random
print("Welcome to PyPassword Generator!")
letters = int(input("How many letters would you like in your password?"))
symbols = int(input("Hoy many symbols would you like?"))
numbers = int(input("How many numbers would you like?"))

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':',
                ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']

generador = ""
for l in range(letters):
    generador += random.choice(list_letters)
for s in range(symbols):
    generador += random.choice(list_symbols)
for n in range(numbers):
    generador += random.choice(list_number)
list_password = list(generador)
shuffle_list = random.shuffle(list_password)
password = "".join(list_password)
print(f"Here is your password: {password}")
