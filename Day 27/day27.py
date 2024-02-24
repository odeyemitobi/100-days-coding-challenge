student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
num_students = 0

for height in student_heights:
    total_height += height
    num_students += 1

average_height = total_height / num_students

rounded_average_height = round(average_height)

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {rounded_average_height}")
