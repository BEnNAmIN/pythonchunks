import random

def diceroll(num_of_rolls):
    rolls = []
    for i in range(num_of_rolls):
        t = random.randint(1,6)
        rolls.append(t)
    rolls.sort()
    print(rolls)

user_num = int(input("How many times should I roll the dice?: "))
diceroll(user_num)
