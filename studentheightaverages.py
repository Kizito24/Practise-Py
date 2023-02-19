student_heights = input("Input a list of student heights").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Write your code below this line

add_result = 0
for height in student_heights:
    add_result += int(height)
print(add_result)

no_of_students = 0
for student in student_heights:
    no_of_students = no_of_students + 1
print(no_of_students)

average = add_result / no_of_students
print(average)
