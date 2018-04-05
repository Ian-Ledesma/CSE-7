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
    def __init__(self, state, name, description, inventory, item, attack, health, magic, location):
        #  Things that a Cat has
        self.state = state
        self.name = name
        self.description = description
        self.inventory = inventory
        self.item = item
        self.attack = attack
        self.health = health
        self.magic = magic
        self.location = location
#  Things that a Cat can do
    def heal(self):
        if self.state == "Eating":
            self.health += 3
            print("You healed")
    def take_damage(self):
        if self.state == "Falling":
            self.health -= 2
            print ("Oof, you fell, you lost 2 HP. You have %s left." %self.health)
        if self.state == "Attacked":
            self.health -= 5
    def interact(self):
        self.state = ""
    def climb(self):
        self.state
    def look(self):
        print(current_node.description)  # current_node is defined in the world map
    def fight(self):
        self.attack ==
    def open(self):
        self.open = open
    def death(self):
        self.health <= 0
        print("Oof. You Died.")

Rock_boi =

# Spongebob = Character("Happy", "Spongebob", "A square, yellow, and porous sponge, gay in his nature.", "Spatula", None,
#                       None, 100)
#
# Squidward = Character("Mad", "Squidward", "A sad blue octopus? He enjoys playing the clarinet and he is simultaneously "
#                                           "arrogant and insecure.", "Clarinet", None, None, 80)
#
# Patrick = Character("Pink", "Patrick", "A pink starfish. In his nature, blissfully ignorant.", "Sand", None, None, 120)
#
# Gary = Character()
