print("The Love Calculator is calculating your score...")
name1 = input("Input your name: ")  # What is your name?
name2 = input("Input your partner's name: ")  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
first_word = (
    (name1 + name2).lower().count("t")
    + (name1 + name2).lower().count("r")
    + (name1 + name2).lower().count("u")
    + (name1 + name2).lower().count("e")
)
second_word = (
    (name1 + name2).lower().count("l")
    + (name1 + name2).lower().count("o")
    + (name1 + name2).lower().count("v")
    + (name1 + name2).lower().count("e")
)

checker = int(str(first_word)  + str(second_word))

if checker <= 10 or checker > 90:
    print(f"Your score is {checker}, you go together like coke and mentos.")
elif checker  >= 40 and checker <= 50:
    print(f"Your score is {checker}, you are alright together.")
else:
    print(f"Your score is {checker}.")
