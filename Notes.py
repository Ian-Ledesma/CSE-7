# print('Hello World')
#
# # Ian Ledesma (Use ctrl +/ to toggle comments)
#
# print(3 + 5)
# print(5 - 3)
# print(5 * 3)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print('See if you can figure this out')
# print(20 % 12 )
#
# #Variable
# car_name = "Weibe Mobile"
# car_type = "Lamborghini Sesto Elemento"
# car_cylinder = 8
# car_mpg = 9000.1
#
# #Inline Printing
# print("My car is the %s." % car_name)
# print("My car is the %s. It is a %s" % (car_name, car_type))
#
# #Taking Input
# name = input("What is your name?")
# print("Hello %s." % name)
# print(name)
#
# age = input("What is your age?")
# print("That's nice, %s." % age)
# print(age)
#
# #Change to the file

def print_hw():
    print("Hello World")


print_hw()


# tab = 4 spaces
def say_hi(name):
    print("Hello %s" % name)
    print ("I hope you will have a fantastic day.")


say_hi("Ian")


def birthday(age):
    age += 1  # age = age + 1

    say_hi("Ian")
    print  ("Ian is 14. Next year:")
    birthday (15)
    