import random

guess_left = 10

word_bank = ["Church", "School", "Respect", "Women", "Cinema", "School Appropriate Beverage", "Character", "Obesity",
             "Life", "School Appropriate Substance"]

rand = random.choice(word_bank)
word = rand.lower()

word_bank.remove(rand)

print(guess_left)

letters_guessed = []

while guess_left > 0:
    output = []
  for letter in word:
      output.append("_")
    else:
        output.append(letter)
    guess = input("guess friend")
    letters_guessed.append(guess)
    str1 = "".join(output)

    if guess == word:
        print("ey")

    else:

        guess_left -= 1

        if str1 == word:
            print("Yeah")
            quit()
    print(letters_guessed)

    print(str1)
    print(guess_left)
    if guess_left == 0:
        print("oof")
        print("the word was %s" % word)

        quit()

print("after you guess the letters press enter")
