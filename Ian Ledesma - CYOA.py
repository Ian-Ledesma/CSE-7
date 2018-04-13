# self.attack = attack
#         self.health = health
# #  Things that a Cat can do
#     def heal(self):
#         if self.state == "Eating Krabby Patty":
#             self.health += 2
#     def take_damage(self):
#         self.health -= 2
#     def interact(self):
#         self.state = ""
#     def climb(self):
#         self.state = ""
#     def look(self):
#         print(current_node.description)
#     def fight(self):
#         self.attack = ""
#     def death(self):
#         self.health <= 0
#         print("Oof. You Died.")
"""
1. import statements
2. class definitions
    a. items
    b. characters/ player
    c. rooms
3. instantiation of classes
    *same order as above
4. controller
"""

class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
#


class Key(Items):
    def __init__(self, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = False


class Time_Machine(Key):
    def __init__(self, name, description, allow_entry):
        super(Time_Machine, self). __init__(self, name, description)
        self.allow_entry = allow_entry
class Clarinet(Key):

class Horse_Radish(Key):
    def __init__(self, name ):
    def open(self):
        if self.unlock:
            print("U opened it lmao XD dead inside")
            self.unlock = True


class Weapons(Items):
    def __init__(self, name, description, attack):
        super(Weapons, self). __init__(name, description)
        self.sand = sand
        self.attack = attack
        self.spatula = spatula
        self.neptune_spatula = neptune_spatula
        self.hydrodynamic_spatula = hydrodynamic_spatula
        self.le_spatula = le_spatula
        self.ladle = ladle
        self.spoon = spoon
#  Done


class Magic(Weapons):
    def __init__(self, name, description, attack, mana_use):
        super(Magic, self). __init__(name, description, attack)
        self.mana_use = mana_use
        self.wand = wand
        self.hocus_pocus_kit = hocus_pocus_kit
        self.magic_conch = magic_conch
        self.imagination_box = imagination_box


class Armor(Items):
    def __init__(self, name, description, defense):
        super(Armor, self). __init__(name, description)
        self.defense = defense
        self.metal = metal
        self.sponge_absorbtion = sponge_absorbtion
        self.fat_flabs = fat_flabs
        self.krab_shell = krab_shell


class Spikes(Armor):
    def __init__(self, name, description, defense, attack):
        super(Spikes, self).__init__(name, description, defense)
        self.attack = attack
        self.sponge_abrasion = sponge_abrasion
        self. pufferfish_spikes = pufferfish_spikes
        self.sea_urchin_spikes = sea_urchin_spikes
#  Done


class Heal(Items):
    def __init__(self, name, description, Heal):
        super(Heal, self). __init__(name, description)
        self.heal = heal

class Imagination(Heal):
class Krabby_Patty (Heal) = Krabby_Patty
        self.filter_feed = filter_feed
        self.mayo = mayo

    def heal(self):
        self.state = "Eating" #Defined in character
#  Done


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
        print(current_node.description)
    def fight(self):
        self.strike == strike

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

'''
The items themselves 
'''
# Temporary Value
current_node = None


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

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
        if self.state == "Eating Krabby Patty":
            self.health += 2
    def take_damage(self):
        self.health -= 2
    def interact(self):
        self.state = ""
    def climb(self):
        self.state = ""
    def look(self):
        print(current_node.description)
    def fight(self):
        self.attack
    def death(self):
        self.health == 0
        print("Oof. You Died.")


extrm1 = Room('South of Pineapple', 'intrm1', None, None, 'extrm2', None, None, "You are near a big metal door on a "
             "pineapple. To the North is a living room, to you south and east is sand, and to your west is a window to a "
             "statue.", )
extrm2 = Room('West of Pineapple', None,  )
extrm3 = Room("North of Pineapple", None, 'extrm4', None, None, None )
extrm4 = Room()
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None,
              "ahead of you are two balloon sofas, 2 fishhooks and a portrait on the wall, a"
              " helmet for a tv, and a blue bamboo wall. to the east is a closet, and to the north is a kitchen.")
intrm2 = Room('Kitchen', 'extrm1', 'intrm2', None, None, None, None, "there's a kitchen with a metal wall to one"
            "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a sink")
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a matal rimmed, circle window."
              "north, outside of it is the outdoors.")
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "you see a collection of party supplies, cooking "
            "supplies, and other supplies of literally anything else. we-a-st of you is a small door, leading to"
            "someone else's room ...")
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "you're on a bamboo ladder, with the only places "
              "to go being up or down." )
intrm6 = Room('Bedroom', )
#  do description
intrm7 = Room('Library', None, None, None, None, 'intrm6', None,)
#  do description
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
            "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world")
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "you walk o" #  not done
intrm10 = Room('Restroom', 'intrm11', None, 'Intrm9', None, None, None, )
intrm11 = Room('Restroom Window', 'extrm3', 'intrm10', None, None, None, None, "outside of the window is a sandy floor,"
                                    "with a city far off into the distance south is a 2 story fall to the outer world")
intrm12 = Room('kitchen window', None, 'extrm1', None, "intrm10", None, None, "outside of the window is a street, sand"
                " on either side for as afar as the eye can see. Southward is a 2 story fall to the outer world" )
intrm13 = Room('Garage', None, None, 'intrm2', 'extrm2', None, None)
intrm14 = Room
intrm15 = Room
intrm16 = Room

current_node = extrm1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        #  Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions [pos]
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        try:
            current_node.move(command)
    except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized")
    print()

sand = Weapons("Sand", "The grains of sand below your perambulation appendages are your weapon.", 2)
spatula = Weapons("Spatula", "The ultimate kitchen appliance is your weapon, the spatula.", 20*3)
neptune_spatula = Weapons("Neptune's Spatula", "The spatula indicating divine culinary potential is your weapon.", 55)
hydrodynamic_spatula = Weapons("Hydro-Dynamic Spatula", "A multi-use spatula with utilities such as triple action" 
                               "cooking, a bright, blinking, red light, and more, it is fit for only the most masterful"
                               "of chef.", 20*3)
ladle = Weapons("Ladle", "A long, angled spoon is the pinnacle multi-utility, but for your use only a weapon", 20)
spoon = Weapons("Spoon", "The average scoop.", 10)
le_spatula = Weapons("Le Spatula", "A spatula so full of itself that it'll hurt YOU, unless you're a fanciful "
                     "character")
#  Turn into a class for the either does takes away your health, or helps you a lot

#  magic
wand = Magic("Magic", "A black stick and star on the tip is your weapon.", 15, 10)
hocus_pocus_kit = Magic("Mr.Magic's Magical Kit", "This kit includes a Book of Spells, a Wand of Whimsy, the beard of"
                        " Rasputin, and a license to practice magic. It possesses the ability to turn anything into"
                        "mayonnaise", 45, 90)
#  Be abl to transform enemy into mayo
magic_conch = Magic("Magic Conch", "This conch gives you the ultimate advice, telling you how to effectively knock out "
                    "an enemy", 9999, 9999)
imagination_box = Magic("Imagination Box", "This box gives you as much power as you give it. In this case only 50.", 50,
                        30)

#  armor
sea_urchin_spikes = Spikes("Sea Urchin Spikes", "A set of spikes for both protection and defense.", 4, 10)
metal = Armor("Anti-Rust Metal", "Just some metal that doesn't rust", 5)
sponge_absorbtion = Armor("Spongebob's Sponginess", "Spongebob's sponginess reduces damage dealt.", 1)
fat_flabs = Armor("Patrick's Fat", "Patrick's fat protects him.", 2)
krab_shell = Armor("Mr.Krabbs' Shell", "Mr. Krabb's molted shell protects is an apt set of armor.", 10)
sponge_abrasion = Spikes("Spongebob's Abrasive Side", "Spongebob's abrasive side barks and bites", -2, 11)
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.", 3, 3)

#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.", )
Krabby_Patty = Heal("Krabby Patty", "The ultimate food instils belief and health.")
Filter_Feed = Heal("Filter Feed", "The water contains healing energies you can use")
