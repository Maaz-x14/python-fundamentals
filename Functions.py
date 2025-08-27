def addition(first_num: int, second_num: int):
    result = first_num + second_num
    return result


print(addition(5, 10))  # These are positional arguments, position matters in this
print(addition(second_num=11, first_num=20))  # These are keyword arguments, position does not matter
