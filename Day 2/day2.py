def calculate_gpa(average_score):
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    course_grade_points = [grade_points.get(grade, 0.0) for grade in grades]

    gpa = sum(course_grade_points) / len(course_grade_points)

    return gpa


def calculate_cgpa(cgpa_list):
    cgpa = sum(cgpa_list) / len(cgpa_list)
    return cgpa


num_courses = 8
course_scores = []
grades = []

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

grades.append(grade)



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

gpa = calculate_gpa(average_score)
print(f"GPA: {gpa:.2f}")

cgpa_list = [gpa]

cgpa = calculate_cgpa(cgpa_list)
print(f"CGPA: {cgpa:.2f}")
