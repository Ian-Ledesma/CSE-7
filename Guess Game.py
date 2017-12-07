import random
num = (random.randint(0, 51))
print(num)

guess = input("Pick a number between 0 and 50")

while guess != num:
    if int(guess) > int(num):
        print("Come now, a bit HIGHER")
    if int(guess) < int(num):
        print("Woah there! a bit LOWER.")

# Get a number
# Get a number (input) from the user
# Compare number to input
# Add "higher or "lower"
# Add 5 guesses
# >Add variable to the # of iterations