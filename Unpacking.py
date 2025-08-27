Coordinates = (1, 2, 3)
# Unpacking can be used to assign values of tuples or lists in just one line
# Instead of Coordinates[0] * Coordinates[1] * Coordinates[2]
# We can use x = Coordinates[0] , y = Coordinates[1] , z = Coordinates[2]
# OR we can also use
x, y, z = Coordinates
print(y * z + x)
# If elements are more u can use asterik(*) with element to unpack a var and make it a list
Values = (1, 2, 3, 4, 5, 6)
a, b, *c = Values
print(c)