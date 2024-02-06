print("Welcome to my tip calculator")

total_bill = float(input("What was the total bill: $"))
percentage_tip =  int(input("Enter the percentage tip you would like to give (10, 12, 15): ")) /100 #converts user input into decimal form.
num_people = int(input("How many people shared this bill? "))

cost = total_bill * percentage_tip
total_cost =  cost + total_bill
per_person_cost = total_cost / num_people
print (f"Each person should pay: ${per_person_cost:.2f}")