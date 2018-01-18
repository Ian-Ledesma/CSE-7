import random

money = 15

rounds = 0

most_money = 0

that_round = 0

while money > 0:

    die_01 = (random.randint(1, 6))
    die_02 = (random.randint(1, 6))
    roll = (die_01 + die_02)

    if roll == 7:
        money += 4
        rounds += 1

        if most_money < money:
            most_money = money
            that_round = rounds

    elif roll != 7:
        money -= 1
        rounds += 1

print("You've got %s dollars" % money)
print("You played %s rounds" % rounds)
print("The most you had was %s bucks." % most_money)
print("You were at roll %s." % that_round)
print("Are you dumb? You're broke. You should never gamble. Idiot.")
