from random import randint
choice = int(
    input("What do you choose? Type 0 to Rock, 1 for Paper or 2 for Scissors."))
if choice < 0 or choice > 2:
    choice = int(
        input("What do you choose? Type 0 to Rock, 1 for Paper or 2 for Scissors."))

computer_choice = randint(0, 3)

if choice == 2:
    player = "scissors"
elif choice == 0:
    player = "rock"
else:
    player = "paper"

if computer_choice == 2:
    pc = "scissors"
elif computer_choice == 0:
    pc = "rock"
else:
    pc = "paper"

if player == pc:
    print("Empate")

if player == "rock":
    if pc == "scissors":
        print("Tu Ganas!")
    if pc == "paper":
        print("Perdiste")

if player == "paper":
    if pc == "scissors":
        print("Perdiste")
    if pc == "rock":
        print("Tu Ganas!")

if player == "scissors":
    if pc == "rock":
        print("Perdiste")
    if pc == "paper":
        print("Tu Ganas!")
print(f"Jugador eligio: {player}: \n Computadora eligio: {pc}  ")
