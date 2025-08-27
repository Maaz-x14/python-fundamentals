array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array[0][1] = 14
print(array)
for row in array:
    for item in row:
        print(item)