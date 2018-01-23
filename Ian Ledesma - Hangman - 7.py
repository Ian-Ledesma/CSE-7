import random

turns = 10
the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_bank = ["Church", "School", "Respect", "Women", "Cinema", "School_Appropriate_Beverage", "Character", "Obesity",
             "Life", "School_Appropriate_Substance"]
List_form = []
letters_guessed = []

random.choice(word_bank)
print(random.choice(word_bank))

guess = input("Guess beesh.")
print("%s? Perhaps..." % guess)

letters_guessed.append(input)
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
