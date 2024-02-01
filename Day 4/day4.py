print("Welcome to my password generator")
fname = input("What is your name: \n")
nick_name = input("What is your nickname: \n")
fav_number = input("Your favorite number is: \n")

name_char = list(fname)
nickname_char = list(nick_name)
fav_number_char = list(fav_number)

combined_char = [
    char
    for pair in zip(name_char, nickname_char, fav_number_char)
    for char in pair
]

while len(combined_char) < 8:
    pseudo_random_digit = str(
        (ord(combined_char[0]) * len(combined_char)) % 10
    )
    combined_char.append(pseudo_random_digit)

combined_char[0] = combined_char[0].capitalize()

generated_password = "".join(combined_char)

print(f"Your generated password is: {generated_password}")
