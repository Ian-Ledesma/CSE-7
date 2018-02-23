# # # Defining Functions
# # def hello_world():
# #     print("Hello World!")
# #
# #
# # hello_world()
# #
# #
# # def square_it(number):
# #     return number ** 2
# #
# #
# # print(square_it(3))
# #
# # for i in range(5):
# #     print(square_it(i))
# #
# #
# # def tip_calc(subtotal):
# #     tip_amt = subtotal * 0.18  # tip_at is a local variable
# #     print("The tip amount is $ %s " %tip_amt)
# #     return tip_amt
# #
# #
# # def total_bill(subtotal):
# #     total = subtotal + tip_calc(subtotal)
# #     return total
# #
# #
# # print(total_bill(100))
# #
# #
# # def distance(x1, y1, x2, y2):
# #     inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
# #     answer = inside ** 0.5
# #     return answer
# #
# #
# # print(distance(0, 0, 3, 4))
# #
# #
# # def pythagorean()
#
# #  Defining a class
# class Cat(object):
#     # TWO underscores before and after
#     def __init__(self, color, pattern):
#         #  Things that a Cat has
#         self.color = color
#         self.pattern = pattern
#         self.state = "happy"
#         self.hungry = False
#
#     #  Things that a Cat can do
#     def jump(self):
#         self.state = "Scared"
#         print("The cat jumps in the air")
#
#     def play(self):
#         self.state = "happy"
#         print("You play with the cat")
#
#
# #  Instantiating (creating) two cats
# cute_cat = Cat("brown", "Spots")
# cute_cat2 = Cat("gray", "no spots")
#
# #  Getting information about the cats
# print(cute_cat.color)
# print(cute_cat2.state)
# print(cute_cat2.color)
#
# cute_cat.jump()
# print(cute_cat.state)
# print(cute_cat2.state)
#
# cute_cat.play()
# print(cute_cat.state)
#
#
# class Car(object):
#     def __init__(self, cilinders, type, color):
#         self.color = color
#         self.type = type
#         self.engineOn = False
#         self.Cilinders = cilinders
#
#     def turn_on(self):
#         if self.engineOn:
#             print("Nothing Happens")
#         else:
#             print ("The engine turns on")
#             self.engineOn = True
#
#     def move_forward(self):
#         if self.engineOn
#             print("You move froward")
#         else:
#             print("nothing happens")
#
#     def turn_off(self):
#         if self.engineOn = False:
#             print("The engine turns off")
#         else:
#             print("nothing happens")
#
# my_car = Car(4, "Ford", "Gray")
#
# my_car.turn_on()
# my_car.move_forward()
# my_car.turn_off()

#  is-a (inheritance)
#  can (method)
#  has-a (field)

