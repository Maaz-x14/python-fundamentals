import random

print("Welcome to Number Guessing Game!")
random_number = random.randint(0, 50)
number = -1
tries = 0
while number != random_number:
    number = int(input("Enter number: "))
    tries += 1
    if number < random_number:
        print("Your guess is LOW!")
    if number > random_number:
        print("Your guess is HIGH!")
    if tries == 6:
        print("You Lose")
        print(f"The number was {random_number}")
        break
    elif number == random_number:
        print("You Win")
