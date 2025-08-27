name = input("Enter name: ")
if len(name) < 4:
    print("Must be at least 4 characters")
elif len(name) > 25:
    print("Name cannot be that long")
else:
    print("Accepted")
