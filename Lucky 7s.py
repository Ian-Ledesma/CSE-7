import random
die_01 = (random.randint(1, 6))
die_02 = (random.randint(1, 6))

money = 15

roll = die_01 + die_02

while money == 0:
    if money != 0:
        money -= 1
    if roll == 7:
        money += 5
    if roll != 7:
        money -= 1

print("You've got %s dollars" % money)
