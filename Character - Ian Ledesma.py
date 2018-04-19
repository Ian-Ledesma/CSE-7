
"""

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

"""
#  Defining a class
# class Character(object):
#     # TWO underscores before and after
#     def __init__(self, state, name, description, inventory, item, attack, health, stats):
#         #  Things that a Cat has
#         self.state = state
#         self.name = name
#         self.description = description
#         self.inventory = inventory
#         self.item = item
#
#         print("Oof. You Died.")


#  Defining a class
class Character(object):
    # TWO underscores before and after
    def __init__(self, state, name, description, inventory, item, attack, health, max_hp, magic, location):
        #  Things that a Cat has
        self.state = state
        self.name = name
        self.description = description
        self.inventory = inventory
        self.item = item
        self.attack = attack
        self.health = health
        self.max_hp = max_hp
        self.magic = magic
        self.location = location
#  Things that a Cat can do

    def defend(self):
        if self.state == "Defend":
            self.take_damage -= 0

    def heal(self):
        if self.state == "Eating":
            self.health += 3
            print("You healed")

    def take_damage(self):
        if self.state == "Falling":
            self.health -= 2
            print("Oof, you fell, you lost 2 HP. You have %s left." % self.health)
        if self.state == "Attacked":
            self.health -= 5

    def interact(self):
        self.state = "Interact"
        print("Touch")

    def climb(self):
        self.state = "Climb"

    def look(self):
        print(current_node.description)  # current_node is defined in the world map

    def fight(self):
        self.state == "Fight"

    def open(self):
        self.state = "Open"

    def death(self):
        self.health <= 0
        print("Oof. You Died.")


Spongebob = Character("Happy", "Spongebob", "A square, yellow, and porous sponge, gay in his nature.", "Spatula", None,
                       0, 100, 100, 130, "extrm1")  # extrm1 defined in map


Squidward = Character("Sad", "Squidward", "A sad blue octopus. He enjoys playing the clarinet, and he is"
                      "simultaneously arrogant and insecure.", None, "Clarinet", 0, 80, 80, 130, )

Patrick = Character("Pink", "Patrick", "A pink starfish. In his nature, blissfully ignorant.", None, "Sand", 15, 120,
                    120, 150, )
# Gary = Character()
