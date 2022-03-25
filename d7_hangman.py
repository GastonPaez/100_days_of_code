import random
words_list = ["estado", "unidad", "embarcacion", "imaginacion", "alambrado", "montura",
              "berenjena", "corbata", "monasterio", "repercusion", "incendio", "invierno"]
word = random.choice(words_list)
print(word)
blanks = len(word)
generate_blanks = "_ " * blanks
print(generate_blanks)

life = 5
while life != 0:
    answer = input("Type a word: ")
    life = 5
    if answer in word:
        print("yes")
    else:
        print("no")
        life = life - 1


life_0 = print("""

  +---+
  |   |
      |
      |
      |
      |
      |
===========
""")
life_1 = print("""

  +---+
  |   |
  0   |
      |
      |
      |
      |
===========
""")
life_2 = print("""

  +---+
  |   |
  0   |
  |   |
      |
      |
      |
===========
""")

life_3 = print("""

  +---+
  |   |
  0   |
 /|   |
      |
      |
      |
===========
""")
life_4 = print("""
  +---+
  |   |
  0   |
 /|\  |
      |
      |
      |
===========
""")
life_5 = print("""

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
      |
===========
""")
life_6 = print("""

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
      |
===========
GAME OVER
""")
