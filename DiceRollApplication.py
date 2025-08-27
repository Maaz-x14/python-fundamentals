import random


class Dice:
    def rollDice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = (dice1, dice2)
        return result

firstRoll = Dice()
secondRoll = Dice()
thirdRoll = Dice()
print(firstRoll.rollDice())
print(secondRoll.rollDice())
print(thirdRoll.rollDice())
