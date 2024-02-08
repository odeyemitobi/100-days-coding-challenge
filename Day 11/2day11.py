print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size do you want: ")  # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? ")  # Do you want pepperoni? Y or N
extra_cheese = input("Do  you want extra cheese? ")   # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
add_pepperoni_small = 2
add_pepperoni_big = 3
no_pepperoni = 0
add_cheese = 1
no_extracheese = 0

price = 0

if size == "S":
    price += small_pizza
elif size == "M":
    price += medium_pizza
elif size == "L":
    price += large_pizza
else:
    print("Invalid entry. Please enter S, M, or L.")

if add_pepperoni == "Y":
    if size == "S":
        price += add_pepperoni_small
    elif size == "M" or size == "L":
        price += add_pepperoni_big
elif add_pepperoni == "N":
    price  += no_pepperoni
else:
    print("Invalid entry. Please enter Y or N.")


if extra_cheese == "Y":
    price  += add_cheese
elif extra_cheese == "N":
    price  += no_extracheese
else:
    print("Invalid entry. Please enter Y or N.")


print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${price}.")