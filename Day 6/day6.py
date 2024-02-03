"""Creating a list"""

fruits = ["apple", "orange", "banana", "grape"]

"""Accessing elements in a list"""
first_fruit = fruits[0]
print(first_fruit)  # Output: 'apple'

"""Modifying elements in a list"""
fruits[1] = "kiwi"
print(fruits)


"""Creating strings"""
greeting_single_quotes = "Hello, Toby!"
greeting_double_quotes = "Hi, Toby!"

"""Concatenating strings"""
combined_greeting = greeting_single_quotes + " " + greeting_double_quotes
print(combined_greeting)  # Output: 'Hello, Toby! Hi, Toby!'

"""String methods"""
uppercase_greeting = combined_greeting.upper()
print(uppercase_greeting)  # Output: 'HELLO, TOBY! HI, TOBY!'
