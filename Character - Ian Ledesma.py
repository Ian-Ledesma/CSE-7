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
    def __init__(self, state, name, description, inventory, item, attack, health, stats):
        #  Things that a Cat has
        self.state = state
        self.name = name
        self.description = description
        self.inventory = inventory
        self.item = item
        self.attack = attack
        self.health = health
#  Things that a Cat can do
    def heal(self):
        if self.state = "Eating Krabby Patty":
            self.health += 2
    def take_damage(self):
        self.health -= 2
    def interact(self):
        self.state = ""
    def climb(self):
        self.state =
    def look(self):
        print(current_node.description)
    def fight(self):
    def death(self):
        self.health == 0
        print("Oof. You Died.")


Spongebob = Character("Happy", "Spongebob", "A square, yellow, and porous sponge, gay in his nature.", "Spatula", None, None, 100)

