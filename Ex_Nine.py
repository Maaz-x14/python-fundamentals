size = int(input("Enter size of array: "))
print("Enter elements of array: ")
myList = []
for nums in range(size):
    myList.append(int(input()))
print(f"Array is: {myList}")
uniques = []
for number in myList:
    if number not in uniques:
        uniques.append(number)
print(f"Array without duplicates is: {uniques}")