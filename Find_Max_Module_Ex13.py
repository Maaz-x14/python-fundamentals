def find_max_input():
    size = int(input("Enter size of list: "))
    print("Enter elements of list")
    my_array = []
    for index in range(size):
        my_array.append(input())
    print("Elements of list are: ")
    for index in range(size):
        print(my_array[index])
    max_value = my_array[0]
    for index in range(size):
        if my_array[index] > max_value:
            max_value = my_array[index]
    print("Max element in list is:", max_value)


def find_max_args(para_array):
    max_value = para_array[0]
    for index in para_array:
        if index > max_value:
            max_value = index
    print("Max element in list is:", max_value)
