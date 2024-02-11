import json
import datetime

def load_data():
    try:
        with open("expenses.txt", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"expenses": []}
    return data

def save_data(data):
    with open("expenses.txt", "w") as file:
        json.dump(data, file, indent=2)

def log_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {"amount": amount, "category": category, "date": date}
    data["expenses"].append(expense)

    save_data(data)
    print("Expense logged successfully!")

def view_expenses():
    for expense in data["expenses"]:
        print(
            f"Amount: ${expense['amount']}, Category: {expense['category']}, Date: {expense['date']}"
        )

def plot_spending_trend():
    amounts = [expense["amount"] for expense in data["expenses"]]
    dates = [expense["date"] for expense in data["expenses"]]

    print("\nSpending Trend Over Time:")
    for i in range(len(amounts)):
        print(f"Date: {dates[i]}, Amount: ${amounts[i]}")

data = load_data()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Log Expense")
    print("2. View Expenses")
    print("3. Spending Trend Over Time")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        log_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        plot_spending_trend()
    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
