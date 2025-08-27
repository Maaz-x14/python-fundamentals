# Tuples are immutable, they cannot be modified
numbers = (1, 2, 3, 4)
print(numbers[0])

# Convert tuple into list
myList = list(numbers)
myList.remove(2)
print(myList)

