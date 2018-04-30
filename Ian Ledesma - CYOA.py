import random
num = (random.randint(0, 101))
Lives = 5
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
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity


# Key
class Key(Items):
    def __init__(self, name, description, rarity):
        super(Key, self).__init__(name, description, rarity)
        self.unlock = False


class TimeMachine(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(TimeMachine, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry

    # def open(self, character):
    #     character.location = extrm1  # defined in room


class HorseRadish(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(HorseRadish, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry

    def open(self):
        if self.unlock:
            print("U opened it lmao XD")
            self.unlock = True


# Weapons
class Weapons(Items):
    def __init__(self, name, description, rarity, attack):
        super(Weapons, self). __init__(name, description, rarity)
        self.attack = attack


class LeSpatula(Weapons):
    def __init__(self, name, description, rarity, attack, self_harm):
        super(LeSpatula, self). __init__(name, description, attack, rarity)
        self.self_harm = self_harm
    if num > 20:
        self_harm = False
    else:
        self_harm = True


# Magic
class Magic(Weapons):
    def __init__(self, name, description, rarity, attack, mana_use):
        super(Magic, self). __init__(name, description, attack, rarity)
        self.mana_use = mana_use


class Armor(Items):
    def __init__(self, name, description, rarity, defense):
        super(Armor, self). __init__(name, description, rarity)
        self.defense = defense


class Spikes(Armor):
    def __init__(self, name, description, rarity, defense, attack):
        super(Spikes, self).__init__(name, description, rarity, defense)
        self.attack = attack


class Heal(Items):
    def __init__(self, name, description, rarity, heal):
        super(Heal, self). __init__(name, description, rarity)
        self.heal = heal
        self.state = "Eating"


# Character
class Character(object):
    def __init__(self, state, name, description, item, attack, health, max_hp, mana):
        self.state = state
        self.name = name
        self.description = description
        self.item = item
        self.attack = attack
        self.health = health
        self.max_hp = max_hp
        self.mana = mana

    def defend(self):
        if self.state == "Defense":
            self.max_hp = 0

    def heal(self):
        if self.state == "Eating":
            self.health = 0
            print("You healed")

    def take_damage(self):
        if self.state == "Falling":
            self.health = 0
            print("Oof, you fell, you lost 2 HP. You have %s left." % self.health)
        if self.state == "Attacked":
            self.health = 0

    def interact(self):
        self.state = "Interact"
        print("Touch")

    def open(self):
        self.state = "Open"

    def death(self):
        if self.health <= 0:
            print("Oof. You Died.")

    def fight(self, enemy):
        try:
            while self.health or enemy.health > 0:
                self.health -= enemy.attack
                enemy.health -= self.attack
                print(Spongebob.health)
                print(enemy.health)
        except AttributeError:
            print('There is no enemy here.')


# inventory
class Inventory:
    def __init__(self, weapon, armor, key, magic, heal):
        self.weapon = weapon
        self.armor = armor
        self.key = key
        self.magic = magic
        self.heal = heal


"""
Room
"""


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, enemy_in):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.enemy_in = enemy_in

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


'''
Item Instantiation 
'''
sand = Weapons("Sand", "The grains of sand below your perambulation appendages are your weapon.", "Common", 5)
spatula = Weapons("Spatula", "The ultimate kitchen appliance is your weapon, the spatula.", "Uncommon", 20*3)
neptune_spatula = Weapons("Neptune's Spatula", "The spatula indicating divine culinary potential is your weapon.",
                          "Legendary", 55)
hydrodynamic_spatula = Weapons("Hydro-Dynamic Spatula", "A multi-use spatula with utilities such as triple action" 
                               "cooking, a bright, blinking, red light, and more, it is fit for only the most masterful"
                               "of chef.", "Legendary", 20*3)
ladle = Weapons("Ladle", "A long, angled spoon is the pinnacle multi-utility, but for your use only a weapon", "Rare",
                20)
spoon = Weapons("Spoon", "The average scoop.", "Rare", 10)
le_spatula = LeSpatula("Le Spatula", "A spatula so full of itself that it'll attack whoever sees fit.", "Epic", 60, 20)
#  magic
wand = Magic("Magic", "A black stick and star on the tip is your weapon.", "Common", 15, 10)
hocus_pocus_kit = Magic("Mr.Magic's Magical Kit", "This kit includes a Book of Spells, a Wand of Whimsy, the beard of"
                        " Rasputin, and a license to practice magic. It possesses the ability to turn anything into"
                        "mayonnaise", "Rare", 45, 90)
#  Be able to transform enemy into mayo
magic_conch = Magic("Magic Conch", "This conch gives you the ultimate advice, telling you how to effectively knock out "
                    "an enemy", "Legendary", 9999, 100)
imagination_box = Magic("Imagination Box", "This box gives you as much power as you give it. In this case only 50.",
                        "Epic", 50, 30)
#  armor
sea_urchin_spikes = Spikes("Sea Urchin Spikes", "A set of spikes for both protection and defense.", "Common", 4, 10)
metal = Armor("Anti-Rust Metal", "Just some metal that doesn't rust", "Uncommon", 5)
sponge_absorbtion = Armor("Spongebob's Sponginess", "Spongebob's sponginess reduces damage dealt.", "Legendary", 20)
fat_flabs = Armor("Patrick's Fat", "Patrick's fat protects him.", "Common", 2)
krab_shell = Armor("Mr.Krabb's Shell", "Mr. Krabb's molted shell protects is an apt set of armor.", "Epic", 10)
sponge_abrasion = Spikes("Spongebob's Abrasive Side", "Spongebob's abrasive side barks and bites", "Uncommon", -2, 11)
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.", "Legendary", 20,
                           11)
#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.", "Rare", 10)
Krabby_Patty = Heal("Krabby Patty", "The ultimate food instills belief and health into the consumer.", "Epic", 20)
Filter_Feed = Heal("Filter Feed", "The water contains healing energies you can use", "Common", 2)
Mayo = Heal = ("Mayonnaise", "The ultimate substance, capable of preserving fish for eons.", 50, "Legendary")

"""
Characters Instantiation
"""
Spongebob = Character("Happy", "Spongebob", "A square, yellow, and porous sponge, gay in his nature.", 10, 100, 100,
                      130, 120)
Squidward = Character("Sad", "Squidward", "A sad blue octopus. He enjoys playing the clarinet, and he is"
                      "simultaneously arrogant and insecure.", 0, 80, 80, 130, 120)
Patrick = Character("Pink", "Patrick", "A pink starfish. In his nature, blissfully ignorant.", "", 120, 120, 150, 120)
Plankton = Character("Brown", 'Amoeba', 'A dog.', 'karen', 10, 10, 10, 100000)
# Karen = Character()
# Nematodes = Character ()
Gary = Character("Snail", "Gary the Snail", "A snail", 20, 40, 40, 5, 300)


"""
Room Instantiation
"""
extrm1 = Room('South of Pineapple', 'intrm1', None, None, 'extrm2', None, None, "You're near a big metal door on a"
              "pine apple.\n North is a living room, south is a road, east is sand, and west is a window into "
              "Squidward's house.", None)
extrm2 = Room('West of Pineapple', None, None, "intrm13", None, None, None, "You're near a massive "
              "pineapple\n where eastward is back to the garage, westward is an easter-island-statue-house, and south "
              "is the road.", None)
#  make road and squidward's house later
extrm3 = Room("North of Pineapple", None, 'extrm4', None, None, None, None, "Around you is sand, all but the window "
              "southward.", None)
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None, "In front of you is a room lined with fishing "
              "and swimming equipment as furniture, helmet for a tv, and a blue bamboo wall.\n To the east is a closet,"
              "and to the north is a kitchen.", Plankton)
intrm2 = Room('Kitchen', 'extrm1', 'intrm2', None, None, None, None, "There's a kitchen with a metal wall to one"
              "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a "
              "sink.\n Northward is the window, southward is the living room, eastward is another window, ", None)
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a metal rimmed, circle window."
              "north, outside of it is the outdoors.", None)
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "There's a collection of supplies for literally"
              "every scenario.\n East is the living room, and West is "
              "someone else's room ...", None)
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "You're on a bamboo ladder, "
              "\n with the only places "
              "to go being up or down.", None)
intrm6 = Room('Bedroom', "intrm8", None, "#hallway", None, None, "intrm7", "The room has red bamboo wallpaper on the "
              "right side and blue metal wallpaper on the left.", None)
intrm7 = Room('Library', None, None, None, None, 'intrm6', None, "All around you are books, and a recliner in the "
              "middle of it all.", None)
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
              "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world", None)
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "", None)
intrm10 = Room('Restroom', 'intrm11', None, 'intrm9', None, None, None, "Around you is a green, floral wall, with a tub"
               "toilet, sink, and a wringer.\n Northward is a window.", None)
intrm11 = Room('Restroom Window', 'extrm3', 'intrm10', None, None, None, None, "outside of the window is a sandy floor,"
               "with a city far off into the distance. \n South is a 2 story fall to the outer world", None)
intrm12 = Room('Kitchen Window', None, 'extrm1', None, "intrm10", None, None, "outside of the window is a street, sand"
               " on either side for as afar as the eye can see. Southward is a 2 story fall to the outer world.", None)
intrm13 = Room('Garage', None, None, 'intrm2', 'extrm2', None, None, "A metal walled room, with tools one one of them"
               "and a large, mobile door.\n Westward is the outdoors, eastward is a return to the hell of a demented "
               "mind.", None)
intrm14 = Room("Gary's Shell", None, None, "intrm4", "maze1", None, None, "You enter the pink snail shell and find a"
               "book shelf, a fire place, a recliner. \n Westward, toward the chair, is the snail with a gaze to shake "
               "the most mighty of warriors.", None)
intrm15 = Room("Cellar", None, None, None, None, "intrm 5", None, "You see many barrels filled with root beer, from "
               "floor to ceiling,\nwith the only way out being up.", None)
intrm16 = Room("Sunroof", "extrm3", "extrm1", None, "extrm2", None, "intrm6", "Around you are some big pineapple leaves"
               "and no ceiling.\n All around is a path to freedom, or a painful retreat downward.", None)
#  Maze Gary
maze1 = Room("Gary's Mind", None, None, None, "maze2", None, None, "A disgustingly colorful expansion surrounds"
             " you., None", None)
maze2 = Room("GAry's Mind", None, "maze3", None, None, None, None, "A disgustingly colorful expansion surrounds"
             "you.", None)
maze3 = Room("GaRy's Mind", None, None, "maze4", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze4 = Room("GarY's Mind", None, None, "maze5", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze5 = Room("Gary'S Mind", None, "maze6", None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze6 = Room("Gary's MInd", "maze7", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze7 = Room("Gary's MiNd", None, None, None, None, None, "maze8", "A disgustingly colorful expansion surrounds"
             " you.", None)
maze8 = Room("Gary's MinD", "intrm5", None, None, None, None, None, "A dark void surrounds you.\n but North is a"
             "brilliant light of ignorance and stupidity, in this void of acknowledgement and intelligence.", None)
#  Maze Spongebob
maze9 = Room("Spongebob's Mind", "maze10", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze10 = Room("SPongebob's Mind", None, "maze11", None, None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze11 = Room("SpOngebob's Mind", None, None, None, "maze12", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze12 = Room("SpoNgebob's Mind", None, None, None, "maze13", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze13 = Room("SponGebob's Mind", None, None, None, None, None, "maze14", "A disgustingly colorful expansion surrounds"
              " you.", None)
maze14 = Room("SpongEbob's Mind", None, None, None, None, "maze15", None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze15 = Room("SpongeBob's Mind", None, None, "maze16", None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze16 = Room("SpongebOb's Mind", None, None, None, None, None, "maze17", "A disgustingly colorful expansion surrounds"
              " you.", None)
maze17 = Room("SpongeboB's Mind", None, None, None, None, "maze18", None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze18 = Room("Spongebob'S Mind", None, None, None, None, None, "extrm2", "A disgustingly colorful expansion surrounds"
              " you.\n But above is relative darkness to this terrifying realm.", None)

# 4. Controller
# current_node = None  # Temporary Value
respawn_point = intrm1
current_node = extrm1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
short_actions = ['a', 'h', 'c', 'h', 'l', ]
all_commands = ['north', 'south', 'east', 'west', 'up', 'down', "fight", "heal", "conjuring", "heal", "look"]

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)

    if command == "look":
    # print the curretn node
    if command == 'fight':
        Spongebob.fight(current_node.enemy_in)

    elif command in short_directions:
        #  Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    elif command not in all_commands:
        print("Command not recognized")
