import random

guess_left = 10

word_bank = ["Church", "School", "Respect", "Women", "Cinema", "School Appropriate Beverage", "Character", "Obesity",
             "Life", "School Appropriate Substance"]

rand = random.choice(word_bank)
word = rand.lower()

word_bank.remove(rand)


letters_guessed = []
output = []

num_of_letters = len(word)
print("The word is %s characters long." % num_of_letters)

while guess_left > 0:
    print(guess_left)
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)

        else:
            output.append("_")

    guess = input("guess friend")
    letters_guessed.append(guess)

    str1 = "".join(output)

    if guess == word:
        print("ey")
        print("You've %s turns left" % guess_left)
        output.append(word)
        print(output)
    else:
        guess_left -= 1
        print("You've %s turns left" % guess_left)
        print(output)

        if str1 == word:
            print("Yeah")
            quit()
    print(letters_guessed)

    print(str1)
    if guess_left == 0:
        print("oof")
        print("the word was %s" % word)

        quit()

print("after you guess the letters press enter")