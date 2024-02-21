def sum_array(arr):
    if not arr or len(arr) < 3:
        return "Array should have at least three elements."

    try:
        arr = list(map(int, arr))
    except ValueError:
        return "Invalid input. Please enter valid numbers."

    highest = max(arr)
    lowest = min(arr)

    result_sum = sum(num for num in arr if num != highest and num != lowest)

    return result_sum

user_input = input("Enter space-separated numbers: ")
input_array = user_input.split()
result = sum_array(input_array)
print(result)
