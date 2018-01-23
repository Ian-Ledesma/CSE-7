import random
num = (random.randint(0, 51))

guess = input("Pick a number between 0 and 50")
turns = 5

# Describes ONE turn. The while loop is the game controller.
while guess != num:
    if guess > str(num):
        print("Come now, a bit HIGHER")
        turns -= 1
    if guess < str(num):
        print("Woah there! a bit LOWER.")
        turns -= 1
    if guess == str(num):
        print("YO! You did it!")
        turns -= 1


    if turns == 0:

# >Add 5 guesses
# >Add variable to the # of iterations
