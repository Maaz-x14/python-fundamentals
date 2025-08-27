weight = int(input("Enter weight: "))
typeWeight = input("(L)bs or (K)gs: ")
newType = typeWeight.upper()
if newType == 'L':
    weight /= 2.205
    print(f"Weight in kgs is: {weight}")
elif newType == 'K':
    weight *= 2.205
    print(f"Weight in lbs is: {weight}")
else:
    print("Please enter correct type")