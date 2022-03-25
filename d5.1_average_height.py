student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

contador = 0
total_height = 0
for h in student_heights:
    contador += 1
    total_height += h

print(f"The average height is {total_height // contador}")
