def addition(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    return first / second


first_input = int(input("Enter the first number: "))
bodmas = input("Choose a bodmas (+, -, *, /): ")
second_input = int(input("Enter the second number: "))

if bodmas == "+":
    result = addition(first_input, second_input)
elif bodmas == "-":
    result = subtraction(first_input, second_input)
elif bodmas == "*":
    result = multiplication(first_input, second_input)
elif bodmas == "/":
    result = division(first_input, second_input)
else:
    result = "Error!"

print(f"{first_input} {bodmas} {second_input} = {result}")
