import random

money = 15

rounds = 0

while money > 0:
    die_01 = (random.randint(1, 6))
    die_02 = (random.randint(1, 6))
    roll = (die_01 + die_02)

    if roll == 7:
        money += 4
        rounds += 1
    elif roll != 7:
        money -= 1
        rounds += 1

print("You've got %s dollars" % money)
print("YOur highest amount of money is $ %s" %)
print("You played %s rounds" % rounds)