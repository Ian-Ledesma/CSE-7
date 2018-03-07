'''
Name
Description
Dialogue?
Inventory
Interact
Move?
Climb
Look
Item
Fight
Health
Take Damage
Death
Stats
'''


#  Defining a class
class Character(object):
    # TWO underscores before and after
    def __init__(self, state, name, description, inventory, item, fight, health, takeDamage, stats):
        #  Things that a Cat has
        self.state = state
        self.name = name
        self.description = description
        self.inventory = inventory
        self.item = item

Spongebob = Character(None, Spongebob, "A square, yellow, and porous sponge, gay in his nature.", None, )

    #  Things that a Cat can do
    def interact(self):
        self.state = ""
    def climb(self):
        self.state = 
    def look(self):
        print description()
    def fight(self):
    def death(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "happy"
        print("You play with the cat")
