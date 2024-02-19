def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1  / value2
    else:
        return "Error"


def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)
