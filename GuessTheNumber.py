import random

random_number = random.randint(0,100)
number = int(input("Enter number: "))
while number != random_number:
    if number < random_number:
        print("Your guess is LOW!")
    elif number > random_number:
        print("Your guess is HIGH!")
    else:
        print("Please enter a valid number")
    number = int(input("Enter number: "))
print("Your guess is correct")
