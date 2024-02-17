def mul_by_n(lst, n):
    print("Inputs: ", lst, n)
    result = [x * n for x in lst]
    print("Result: ", result)
    return result


my_list = [1, 2, 3]
multiplier = 4
output = mul_by_n(my_list, multiplier)
print("Final Output: ", output)
