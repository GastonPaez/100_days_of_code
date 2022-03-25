print("Welcome to the Treasure Island. Your Mission is to find the treasure.")
story1 = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'")
if story1.lower() == "left":
    story2 = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if story2.lower() == "wait":
        story3 = input(
            "You alive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if story3.lower() == "yellow":
            print("You Win!")
        else:
            print("You enter a room of the beast. Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
