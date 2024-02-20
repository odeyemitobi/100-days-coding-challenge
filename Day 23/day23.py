students_data = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    grades_input = input("Enter student grades (comma-separated): ")

    grades_list = grades_input.split(",")

    grades = [int(x) for x in grades_list]

    student_info = [name, student_id, grades]
    students_data.append(student_info)

def calculate_average(grades):
    return sum(grades) / len(grades)

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def display_student_info(student_info):
    name, student_id, grades = student_info
    print(f"Student Name: {name}")
    print(f"Student ID: {student_id}")
    print(f"Grades: {grades}")
    print(f"Average Grade: {calculate_average(grades)}")
    print(f"Highest Grade: {find_highest_grade(grades)}")
    print(f"Lowest Grade: {find_lowest_grade(grades)}")
    print()

while True:
    add_student()

    another_student = input("Do you want to add another student? (yes/no): ")
    if another_student.lower() != 'yes':
        break

for student_info in students_data:
    display_student_info(student_info)
