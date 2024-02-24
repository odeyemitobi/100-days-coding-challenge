student_heights = []

while True:
    height_input = input("Enter student height (type 'd' when you are done adding height): ")

    if height_input.lower() == "d":
        break

    for char in height_input:
        if not char.isdigit():
            print("Invalid input. Please enter a valid height.")
            break
    else:
        height = int(height_input)
        student_heights.append(height)

if not student_heights:
    print("No heights entered. Exiting.")
else:
    total_height = sum(student_heights)
    num_students = len(student_heights)

    average_height = total_height / num_students

    rounded_average_height = round(average_height)

    print(f"Total height: {total_height}")
    print(f"Number of students: {num_students}")
    print(f"The average height is: {rounded_average_height}")
