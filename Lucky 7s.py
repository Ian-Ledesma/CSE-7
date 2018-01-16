import random

money = 15

rounds = 0

while money > 0:
    print("Are you dumb? You're broke. You should never gamble. Idiot.")
    die_01 = (random.randint(1, 6))
    die_02 = (random.randint(1, 6))
    roll = (die_01 + die_02)
    best_rounds = 0
    max_money = 0

    if roll == 7:
        money += 4
        rounds += 1
    elif roll != 7:
        money -= 1
        rounds += 1
        if money > max_money:
            money = max_money


        print("You've got %s dollars" % money)
        print("You played %s rounds" % rounds)
        print("You should've stopped at round %s, you had $%s." % (best_rounds, max_money))



