student_scores = input("Input a list of scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

scores = 0
for s in student_scores:
    if s > scores:
        scores = s
print(f"The Highest score in the class is: {scores} ")
