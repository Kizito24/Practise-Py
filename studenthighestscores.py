# Don't change the code below this line
student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
   student_scores[n] = int(student_scores[n])
print(student_scores)
# Write your code below this line

highest_score = 0
for score in student_scores:
    score = int(score)
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")
