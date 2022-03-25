

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
themap = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3} ")
position = input(
    "Where do you want to put the treasure? Type number of column and number of row together. ")

if int(position[1]) == 1:
    row1[int(position[0])-1] = "💰"
elif int(position[1]) == 2:
    row2[int(position[0])-1] = "💰"
else:
    row3[int(position[0])-1] = "💰"

print(f"{row1}\n{row2}\n{row3} ")
