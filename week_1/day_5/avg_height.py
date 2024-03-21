# Goal is to get average height of students from a list of heights
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# student heights
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

# Number of students and then add 1
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

# Average height
average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

# RANGE
# range(start, stop, step)
# range(start, stop)

# for number in range(1, 10):
#     print(number)