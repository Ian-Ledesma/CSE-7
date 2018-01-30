import random

turns = 10
word_bank = ["Church", "School", "Respect", "Women", "Cinema", "School Appropriate Beverage", "Character", "Obesity",
             "Life", "School Appropriate Substance"]
letters_guessed = []

rand = random.choice(word_bank)
random_word = rand.lower()

right_letter = len(random_word)

while turns != 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
            right_letter -= 1
        else:
            output.append("_")
            turns -= 1

    print(output)
    guess = input("Guess beesh.")
    letters_guessed.append(guess)

    print("%s? Perhaps..." % guess)

print(letters_guessed)

"""
Outline of Hangman
1. Make a word bank of whatever - 10 items
2. Select a random item from the list
3. Add user input to a list of letters_guessed
4.Build a list of letters to show, and display the string form
5. Create the win condition

*steps 3 and 4 are done in at the same time if done correctly
"""
