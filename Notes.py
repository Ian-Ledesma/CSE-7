# # # # # print('Hello World')
# # # # #

# # # # # # Ian Ledesma (Use ctrl +/ to toggle comments)
# # # # #

# # # # # print(3 + 5)
# # # # # print(5 - 3)
# # # # # print(5 * 3)
# # # # # print(6 / 2)
# # # # # print(3 ** 2)
# # # # #

# # # # # print()
# # # # # print('See if you can figure this out')
# # # # # print(20 % 12 )
# # # # #

# # # # # #Variable
# # # # # car_name = "Weibe Mobile"
# # # # # car_type = "Lamborghini Sesto Elemento"
# # # # # car_cylinder = 8
# # # # # car_mpg = 9000.1
# # # # #
# # # # # #Inline Printing
# # # # # print("My car is the %s." % car_name)
# # # # # print("My car is the %s. It is a %s" % (car_name, car_type))
# # # # #
# # # # # #Taking Input
# # # # # name = input("What is your name?")
# # # # # print("Hello %s." % name)
# # # # # print(name)
# # # # #
# # # # # age = input("What is your age?")
# # # # # print("That's nice, %s." % age)
# # # # # print(age)
# # # # #
# # # # # #Change to the file
# # # #
# # # # def print_hw():
# # # #     print("Hello World")
# # # #
# # # #
# # # # print_hw()
# # # #
# # # #
# # # # # tab = 4 spaces
# # # # def say_hi(name):
# # # #     print("Hello %s" % name)
# # # #     print ("I hope you will have a fantastic day.")
# # # #
# # # #
# # # # say_hi("Ian")
# # # #
# # # #
# def birthday(age):
# # # # #     age += 1  # age = age + 1
# # # # #
# # # #     say_hi("Ian")
# # # #     print  ("Ian is 14. Next year:")
# # # #     birthday (15)
# # #
# # #
# # # def f(x):
# # #     return x**5 + 4 * x**4 - 17 * x**2 +4
# # #
# # #
# # # print (f(3))
# # # print(f(3) + f(5))
#
#
# If statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # Else if
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#          return "F"
#
#
# Loops
#
#
# for num in range (5):
#         print(num + 1)
#
#
# for letter in "Hello World":
#     print(letter) #dont pick blue words #Any varaible is fine

# a = 1
# while a < 10:
#     print (a)
#     a += 1


response = ""
while response != "Hello":
    response = input("Say\"Hello\"")

print("Hello \nWorld")  #\n means newline

import random  #imports should be at the top of the code

print(random.randint(0, 6))
