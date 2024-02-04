print("Welcome to My To-Do List!")

todo_list = []

def mark_task(todo_list, done_sucessfully):
    if not todo_list:
        print("Your to-do list is empty. No tasks to mark.")
    else:
        print("Your To-Do List: ")
        for index, item in enumerate(todo_list, start=1):
            status = "Done" if item["done"] else "Undone"
            print(f"{index}. {item['task']} - {status}")

        task_index = int(input("Enter the task number to mark: "))
        if 1 <= task_index <= len(todo_list):
            todo_list[task_index - 1]["done"] = done_sucessfully
            status = "Done" if done_sucessfully else "Undone"
            print(f"Task '{todo_list[task_index - 1]['task']}' marked as {status}!")
        else:
            print("Invalid task number. Please enter a valid task number.")


while True:

    print("Menu: ")
    print("1. Add Task")
    print("2. View To-Do List")
    print("3. Mark Task as Done")
    print("4. Mark Task as Undone")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully!")
    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty. Add some tasks!")
        else:
            print("Your To-Do List: ")
            for index, item in enumerate(todo_list, start=1):
                status = "Done" if item["done"] else "Undone"
                print(f"{index}. {item['task']} - {status}")

    elif choice == "3":
        mark_task(todo_list, True)
    elif choice == "4":
        mark_task(todo_list, False)
    elif choice == "5":
        print("Quit Successfully!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
