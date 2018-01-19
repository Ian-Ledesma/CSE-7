import random
the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_bank = ["Church", "School", "Respect", "Women", "Cinema", "Sunshine", "Character", "Obesity", "Drug", "Communism"]

"""
Outline of Hangman
1. Make a word bank of whatever - 10 items
2. Select a random item from the list
3. Hide the word (Replace with *)
4. Reveal letters if they have been guessed
5. Create the win condition

*steps 3 and 4 are done in at the same time if done correctly
"""
random.choice(word_bank)
