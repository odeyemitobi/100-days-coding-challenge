num_courses = 8
course_scores = []

i = 0
while i < num_courses:
    score = float(input(f"Enter score for Course {i + 1}: "))
    course_scores.append(score)
    i += 1

average_score = sum(course_scores) / num_courses

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nAverage Score: {average_score}")
print(f"Grade: {grade}")
