print("Welcome to Tech-titans portal")
user_data = {}  # Dictionary to store user dat
print("type ctrl d or ctrl c to quit the program")

storage = '.database'
import json

def signup():
    try:
        choice = input("Do you want to Sign Up or Sign In: ")

        if choice.lower() == 'sign up':
            user_info = {}  # Dictionary to store individual user's information
            choices = ["fullname", "username", "email"]

            # this senior boy is meant to only execute when choice is equal to sign up
            for usr_input in choices:
                user_info[usr_input] = input(f"Please Enter {usr_input}: ").strip()

            password = input("Create a password: ")
            user_info['password'] = password

            # Use the username as the key in the user_data dictionary
            user_data[user_info['username']] = user_info

            # open a file and write

            with open(storage, "w") as db:
                # db.write(str(user_data))
                json.dump(user_data, db, indent=2)

            print(f"Successfully signed up {user_info['username']}")
        elif choice.lower() == 'sign in':
            signin()
        else:
            print('Invalid Input! Try Again')
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

def signin():
    try:
        username_input = input("Enter your username: ").strip()
        password_input = input("Enter your password: ")

        with open(storage, "r") as db:
            user_data = json.load(db)

            if username_input in user_data:
                if user_data[username_input]['password'] == password_input:
                    print(f"Welcome back, {user_data[username_input]['fullname']}!")
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Username not found. Please sign up if you haven't already.")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


try:
    signup()
except ValueError as ve:
    print(f'Error! ve')
# create a sign in button in the elif choice and use the
# dictionary not the choices.
# create a big dictionary as key and the data as value.