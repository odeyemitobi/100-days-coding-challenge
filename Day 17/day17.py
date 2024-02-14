import random

names_string = "Toby, Bendamxi, Yusufmoney, Damstar, Milo, Shortbread"
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
selected_name = names[random_index]
print(f"{selected_name} is going to buy the meal today!")
