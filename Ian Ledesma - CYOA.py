#  import webbrowser
import random
# webbrowser.open_tab(https://www.youtube.com/watch?v=8xn1hRcu18w)
num = (random.randint(0, 101))
current_node = None  # Temporary Value
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
# Make Spongebob name change to Gooby-Goober Spongebob


class Items(object):
    def __init__(self, name, description, rarity):  # rarity tiers: Common = 1, Uncommon = 2, Rare = 3, Epic = 4,
        self.name = name                            # Legendary = 5
        self.description = description
        self.rarity = rarity


# Key
class Key(Items):
    def __init__(self, name, description, rarity):
        super(Key, self).__init__(name, description, rarity)


class Time(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(Time, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry


def open_time(self):
    while Time in Inventory and Spongebob.location == maze9 and command == "north" or "n":
        Spongebob.location = intrm1
        print("U opened it lmao XD")
        self.unlock = True


class Radish(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(Radish, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry


def open_radish(spongebob):
    while Radish in Inventory and spongebob.location == intrm14 and command == "north" or "n":
        Spongebob.location = intrm15


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


# Heal
class Heal(Items):
    def __init__(self, name, description, rarity, heal):
        super(Heal, self). __init__(name, description, rarity)
        self.heal = heal


# Socks
class Socks(Items):
    def __init__(self, name, description, rarity, fall_soft):
        super(Socks, self). __init__(name, description, rarity)
        self.fall_soft = fall_soft


# Gloves
class Gloves(Items):
    def __init__(self, name, description, rarity, harder_hit):
        super(Gloves, self). __init__(name, description, rarity)
        self.harder_hit = harder_hit


# Character Class
class Character(object):
    def __init__(self, name, description, item, strike, health, max_hp, mana, level, lives, xp, dropxp):
        self.name = name
        self.description = description
        self.item = item
        self.strike = strike
        self.health = health
        self.max_hp = max_hp
        self.mana = mana
        self.lives = lives
        self.level = level
        self.xp = xp
        self.dropxp = dropxp

#  Levels
    def level_up(self):
        if self.xp == 10:
            self.level += 1
        print("You've leveled up.\n %s is now level %s." % Spongebob.name % self.level)

    def defend(self):
        self.max_hp = 0

    def heal(self):
            self.health = 0
            print("You healed")


#  Death
    def death(self):
        self.lives -= 1
        print("Oof. Dang breh %s, is pretty ded." % Character.death(self))


# Game Over
    def game_over(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME OVER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        exit(0)

# Attack
    def attack_enemy(self, character):    # Static is ok
        character.inventory.item_w.attack += character.inventory.item_g.harder_hit and character.strike

# Respawn
def respawn(character):
    global rand_node
    character.health = character.max_hp
    rand_node = current_node


# inventory
class Inventory:
    def __init__(self, weapon, armor, key, magic, heal, gloves, socks):
        self.weapon = weapon
        self.armor = armor
        self.key = key
        self.magic = magic
        self.heal = heal
        self.socks = socks
        self.gloves = gloves


inventory = Inventory(None, None, None, None, None, None, None)

"""
Room
"""


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, enemy_in, item_magic, item_weapon,
                 item_key, item_armor, item_heal, item_socks, item_gloves, space_magic, space_weapon, space_armor,
                 space_key, space_heal, space_socks, space_gloves):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.enemy_in = enemy_in
# Room item
        self.item_m = item_magic
        self.item_w = item_weapon
        self.item_a = item_armor
        self.item_k = item_key
        self.item_h = item_heal
        self.item_s = item_socks
        self.item_g = item_gloves
#  Holding for when you switch item from room to inventory
        self.space_m = space_magic
        self.space_w = space_weapon
        self.space_a = space_armor
        self.space_k = space_key
        self.space_h = space_heal
        self.space_s = space_socks
        self.space_g = space_gloves

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


'''
Item Instantiation 
'''
sand = Weapons("Sand", "The grains of sand below your perambulation appendages are your weapon.\n Common", 1, 5)
spatula = Weapons("Spatula", "The ultimate kitchen appliance is your weapon, the spatula.\n Uncommon", 2, 20*3)
neptune_spatula = Weapons("Neptune's Spatula", "The spatula indicating divine culinary potential is your weapon.",
                          5, 55)
hydrodynamic_spatula = Weapons("Hydro-Dynamic Spatula", "A multi-use spatula with utilities such as triple action" 
                               "cooking, a bright, blinking, red light, and more, it is fit for only the most masterful"
                               "of chef.\n Legendary", 5, 20*3)
ladle = Weapons("Ladle", "A long, angled spoon is the pinnacle multi-utility, but for your use only a weapon\n Rare", 3,
                20)
spoon = Weapons("Spoon", "The average scoop.\n Uncommon", 2, 10)
le_spatula = LeSpatula("Le Spatula", "A spatula so full of itself that it'll attack whoever sees fit.\n Epic", 4, 60,
                       20)
#  magic
wand = Magic("Magic", "A black stick and star on the tip is your weapon.\n Common", 1, 15, 10)
hocus_pocus_kit = Magic("Mr.Magic's Magical Kit", "This kit includes a Book of Spells, a Wand of Whimsy, the beard of"
                        " Rasputin, and a license to practice magic. It possesses the ability to turn anything into"
                        "mayonnaise.\n Rare", 3, 45, 90)
#  Be able to transform enemy into mayo
magic_conch = Magic("Magic Conch", "This conch gives you the ultimate advice, telling you how to effectively knock out"
                    "an enemy.\n Legendary", 5, 9999, 100)
imagination_box = Magic("Imagination Box", "This box gives you as much power as you give it. In this case only 50.\n "
                        "Epic", 4, 50, 30)
#  Gloves
# infinity_gauntlet = Gloves('Infinity Gauntlet', "With the 6 infinity stones, you can end the world in a SNAP.\n"
#                            "Literally JEEZUS", 6, current_node.enemy.health * 1/2)
sterile = Gloves("Don't Touch Me I'm Sterile", "These gloves give you the capacity to be sterile and dangerous.\n "
                 "Common", 3, 20)
#  armor
sea_urchin_spikes = Spikes("Sea Urchin Spikes", "A set of spikes for both protection and defense.\n Common", 1, 4, 10)
metal = Armor("Anti-Rust Metal", "Just some metal that doesn't rust.\n Uncommon", 2, 5)
sponge_absorption = Armor("Spongebob's Sponginess", "Spongebob's sponginess reduces damage dealt.\n Legendary", 5, 20)
fat_flabs = Armor("Patrick's Fat", "Patrick's fat protects him.\n Common", 2, 11)
krab_shell = Armor("Mr.Krabb's Shell", "Mr. Krabb's molted shell protects is an apt set of armor.\n Epic", 4, 10)
sponge_abrasion = Spikes("Spongebob's Abrasive Side", "Spongebob's abrasive tough to both y'all.\n Uncommon", 2, -2, 11)
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.\n Legendary", 5, 20,
                           11)
#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.\n Rare", 3, 10)
Krabby_Patty = Heal("Krabby Patty", "The ultimate food instills belief and health into the consumer.\n Epic", 4, 20)
Filter_Feed = Heal("Filter Feed", "The water contains healing energies you can use.\n Common", 1, 2)
Mayo = Heal("Mayonnaise", "The ultimate substance, capable of preserving fish for eons.\n Legendary", 5, 50)


"""
Characters Instantiation
"""
Spongebob = Character("Spongebob", "A square, yellow, and porous sponge, gay in his nature.", 10, 100, 100,
                      130, 120, 5, 5, 50, 20)
Squidward = Character("Squidward", "A sad blue octopus. He enjoys playing the clarinet, and he is"
                      "simultaneously arrogant and insecure.", 20, 80, 80, 130, 120, 2, 5, 20, 20)
Patrick = Character("Patrick", "A pink starfish. In his nature, blissfully ignorant.", "Fat Flabs", 120, 120,
                    150, 120, 5, 5, 50, 50)
Spot = Character('Spot', 'A dog/amoeba.', None, 10, 10, 10, 1000, 5, 50, 50, 50)
Karen = Character("Karen the Computer", "The computer wife of Sheldon J. Plankton. She has a snarky sense of humor, but"
                  "a caring nature programmed into her by her creator and husband.", None, 100, 120, 130, 170, 30, 10,
                  300, 150)
Nematodes = Character("Nematodes", 'They are pale green and dark green worms. They are lead by one leading nematode '
                      'which calls out things like "hungry," "still hungry," or "thirsty" and leads its followers to '
                      'foods and drinks.', None, 20, 30, 190, 200, 10, 100, 150, 0)
# Squidward = Character("Squidward", "A sad blue octopus. He enjoys playing the clarinet, and he is"
#                       "simultaneously arrogant and insecure.", 55, 80, 80, 130, 120, 1, 5, 10, 10)
# Patrick = Character("Patrick", "A pink starfish. In his nature, blissfully ignorant.", fat_flabs, 120, 120,
#                     150, 120, 0, 5, 0, 15)
# Spot = Character('Spot', 'A dog/amoeba.', None, 10, 10, 10, 1000, 0, 5)
# Karen = Character("Karen the Computer", "The computer wife of Sheldon J. Plankton. She has a snarky sense"
#                   "of humor, but a caring nature programmed into her by her husband.", None, 100, 120, 130, 170, 2, 5,
#                   20, 20)
NeoKaren = Character("Neo-Karen", "The evolved form of Karen the computer, ready to take on any foe, including the "
                     "ultimate foe: Spongebob- Goofy Goober", None, 10000, 10000, 1000, 1000, 100, 2, 1000, 500)
Plankton = Character("Sheldon J. Plankton", "A small, green, evil plankton. He's dead set on getting the krabby patty "
                     "secret formula with the aid of his computer wife, Karen.", wand, 40, 250, 300, 300, 45, 5, 450,
                     220)
# Nematodes = Character ("Mean", "")
Gary = Character("Gary the Snail", "A snail", wand, 300, 300, 300, 300, 50, 5, 3000, 300)


"""
Room Instantiation
"""
"""
Room Instantiation
"""
extrm1 = Room('South of Pineapple', 'intrm1', None, None, 'extrm2', None, None, "You're near a big metal door on a"
              "pine apple.\n North is a living room, south is a road, east is sand, and west is a window into "
              "Squidward's house.", Squidward, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None)
extrm2 = Room('West of Pineapple', None, None, "intrm13", None, None, None, "You're near a massive "
              "pineapple\n where eastward is back to the garage, westward is an easter-island-statue-house, and south "
              "is the road.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
#  make road and squidward's house later
extrm3 = Room("North of Pineapple", None, 'extrm4', None, None, None, None, "Around you is sand, all but the window "
              "southward.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None, "In front of you is a room lined with fishing "
              "and swimming equipment as furniture, helmet for a tv, and a blue bamboo wall.\n To the east is a closet,"
              "and to the north is a kitchen.", None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None)
intrm2 = Room('Kitchen', 'extrm3', 'intrm2', None, None, None, None, "There's a kitchen with a metal wall to one"
              "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a "
              "sink.\n Northward is the window, southward is the living room, eastward is another window, ", None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None)
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a metal rimmed, circle window."
              "north, outside of it is the outdoors.", None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None)
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "There's a collection of supplies for literally"
              "every scenario.\n East is the living room, and West is "
              "someone else's room ...", None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None)
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "You're on a bamboo ladder, "
              "\n with the only place to go being up or down.", None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None)
intrm6 = Room('Bedroom', "intrm8", None, "#hallway", None, None, "intrm7", "The room has red bamboo wallpaper on the "
              "right side and blue metal wallpaper on the left.", None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None)
intrm7 = Room('Library', None, None, None, None, 'intrm6', None, "All around you are books, and a recliner in the "
              "middle of it all.", None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None)
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
              "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world", None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None)
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "", None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None)
intrm10 = Room('Restroom', 'intrm11', None, 'intrm9', None, None, None, "Around you is a green, floral wall, with a tub"
               "toilet, sink, and a wringer.\n Northward is a window.", None, None, None, None, None, None, sterile,
               None, None, None, None, None, None, None, None)
intrm11 = Room('Restroom Window', 'extrm3', 'intrm10', None, None, None, None, "outside of the window is a sandy floor,"
               "with a city far off into the distance. \n South is a 2 story fall to the outer world", None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, None)
intrm12 = Room('Kitchen Window', None, 'extrm1', None, "intrm10", None, None, "outside of the window is a street, sand"
               " on either side for as afar as the eye can see. Southward is a 2 story fall to the outer world.", None,
               None, None, None, None, None, None, None, None, None, None, None, None, None, None)
intrm13 = Room('Garage', None, None, 'intrm2', 'extrm2', None, None, "A metal walled room, with tools one one of them"
               "and a large, mobile door.\n Westward is the outdoors, eastward is a return to the hell of a demented "
               "mind.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
intrm14 = Room("Gary's Shell", None, None, "intrm4", "maze1", None, None, "You enter the pink snail shell and find a"
               "book shelf, a fire place, a recliner. \n Westward, toward the chair, is the snail with a gaze to shake "
               "the most mighty of warriors. You need a key to cross the realm", None, None, None, None, None, None,
               None, None, None, None, None, None, None, None, None)
intrm15 = Room("Cellar", None, None, None, None, "intrm 5", None, "You see many barrels filled with root beer, from "
               "floor to ceiling,\nwith the only way out being up.", None, None, None, None, None, None, None, None,
               None, None, None, None, None, None, None)
intrm16 = Room("Sunroof", "extrm3", "extrm1", None, "extrm2", None, "intrm6", "Around you are some big pineapple leaves"
               "and no ceiling.\n All around is a path to freedom, or a painful retreat downward.", None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, None)
#  Maze Gary
maze1 = Room("Gary's Mind", None, None, None, "maze2", None, None, "A disgustingly colorful expansion surrounds"
             " you., None", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze2 = Room("GAry's Mind", None, "maze3", None, None, None, None, "A disgustingly colorful expansion surrounds"
             "you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze3 = Room("GaRy's Mind", None, None, "maze4", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze4 = Room("GarY's Mind", None, None, "maze5", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze5 = Room("Gary'S Mind", None, "maze6", None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze6 = Room("Gary's MInd", "maze7", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze7 = Room("Gary's MiNd", None, None, None, None, None, "maze8", "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze8 = Room("Gary's MinD", "intrm5", None, None, None, None, None, "A dark void surrounds you.\n but North is a"
             "brilliant light of ignorance and stupidity, in this void of acknowledgement and intelligence.", None,
             None, None, None, None, None, None, None, None, None, None, None, None, None, None)
#  Maze Spongebob
maze9 = Room("Spongebob's Mind", "maze10", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze10 = Room("SPongebob's Mind", None, "maze11", None, None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze11 = Room("SpOngebob's Mind", None, None, None, "maze12", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze12 = Room("SpoNgebob's Mind", None, None, None, "maze13", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze13 = Room("SponGebob's Mind", None, None, None, None, None, "maze14", "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze14 = Room("SpongEbob's Mind", None, None, None, None, "maze15", None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze15 = Room("SpongeBob's Mind", None, None, "maze16", None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze16 = Room("SpongebOb's Mind", None, None, None, None, None, "maze17", "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze17 = Room("SpongeboB's Mind", None, None, None, None, "maze18", None, "A disgustingly colorful expansion surrounds"
              " you.", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
maze18 = Room("Spongebob'S Mind", None, None, None, None, None, "extrm2", "A disgustingly colorful expansion surrounds"
              " you.\n But above is relative darkness to this terrifying realm.", None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None)
nodes = [extrm1, extrm2, extrm3, intrm1, intrm2, intrm3, intrm4, intrm5, intrm6, intrm7, intrm8, intrm9, intrm10,
         intrm11, intrm12, intrm13, intrm14, intrm15, intrm16, maze1, maze2, maze3, maze4, maze5, maze6, maze7, maze9,
         maze10, maze11, maze12, maze13, maze14, maze15, maze16, maze17, maze18]
rand_node = (random.choice(nodes))

# 4. Controller
respawn_point = intrm1
current_node = extrm1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
short_actions = ['a', 'h', 'c', 'h', 'l', ]
all_commands = ['north', 'south', 'east', 'west', 'up', 'down', "fight", "heal", "conjuring", "look", "open"]

while True:
    print(current_node.name)
    command = input('>_').lower().strip()
    # Short commands
    if command in short_directions:
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


#  Quit
    if command == 'quit':
        print("you just died yourself. Lmao XD")
        quit(0)
    if command == "i don't feel so good" or "i don't wanna go":
        print("Thanos just killed half of the universe. You are diagnosed with the ded.")
        quit(0)
#  Look
    if command == "look":  # print the current node
        try:
            print(current_node.description)
            print(current_node.item_m, ",", current_node.item_w, ",", current_node.item_a, ",", current_node.item_k,
                  ",",
                  current_node.item_h, ",", current_node.item_s, ",", current_node.item_g)
            if current_node.enemy_in is not None:
                print(current_node.enemy_in.name)

        except AttributeError:
            print("There's no enemy here.")
#  Attack
    if command == 'fight':
    #   Fighting
#  def fight(self, spongebob, enemy):

        try:
            if current_node.enemy_in is not None:
                enemy = current_node.enemy_in
                print("%s challenges you to a d-d-dd-DUEL!" % enemy.name)
            elif enemy >= 0:
                enemy.lives -= 1
            while Spongebob.health or enemy.health > 0:
                print("%s challenges you to a d-d-dd-DUEL!" % enemy.name)
            if Spongebob.health <= 0:
                print("You lost.")
                Spongebob.death()
                Spongebob.dropxp += enemy.xp
            elif enemy.health <= 0:
                print("You won")
                enemy.dropxp += Spongebob.xp
            while Spongebob.health or enemy.health > 0:
                if Spongebob.mana >= inventory.magic.mana_use:
                    enemy.health -= inventory.magic.attack
                if enemy.mana >= enemy.inventory.magic.mana_use:
                    Spongebob.health -= enemy.inventory.magic.attack
                Spongebob.health -= enemy.attack
                Spongebob.mana += 10
                enemy.mana += 10  # Recharge mana between turn
                enemy.health -= Spongebob.attack_enemy(enemy)
                print("Health:%s /n Mana:%s" % Spongebob.health % Spongebob.mana)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        "~~~~")
                print("Enemy:%s /n Enemy Mana:%s" % enemy.health % enemy.mana)

        except AttributeError:
            print('There is no enemy here.')



    if command == "pick up" or "equip": #Equip
        try:
            if current_node.item_w.rarity >= inventory.weapon.rarity:
                inventory.weapon = current_node.space_w  # copy what you have to space
                current_node.item_w = inventory.weapon  # copy what's in the room to inventory
                current_node.space_w = current_node.item_w  # put what you HAD into the room
                current_node.space_w = None  # clear the space for new stuff

            elif current_node.item_m.rarity >= inventory.magic.rarity:
                inventory.magic = current_node.space_m  # copy what you have to space
                current_node.item_m = inventory.magic  # copy what's in the room to inventory
                current_node.space_m = current_node.item_m  # put what you HAD into the room
                current_node.space_m = None  # clear the space for new stuff

            elif current_node.item_a.rarity >= inventory.armor.rarity:
                inventory.armor = current_node.space_w  # copy what you have to space
                current_node.item_w = inventory.weapon  # copy what's in the room to inventory
                current_node.space_w = current_node.item_w  # put what you HAD into the room
                current_node.space_w = None  # clear the space for new stuff

            elif current_node.item_s.rarity >= inventory.socks.rarity:
                inventory.socks = current_node.space_s  # copy what you have to space
                current_node.item_s = inventory.socks  # copy what's in the room to inventory
                current_node.space_s = current_node.item_s  # put what you HAD into the room
                current_node.space_s = None  # clear the space for new stuff

            elif current_node.item_h.heal >= inventory.heal.heal:
                inventory.heal = current_node.space_h  # copy what you have to space
                current_node.item_h = inventory.heal  # copy what's in the room to inventory
                current_node.space_h = current_node.item_h  # put what you HAD into the room
                current_node.space_h = None  # clear the space for new stuff

            elif current_node.item_g.rarity >= inventory.gloves.rarity:
                inventory.gloves = current_node.space_g  # copy what you have to space
                current_node.item_g = inventory.gloves  # copy what's in the room to inventory
                current_node.space_g = current_node.item_g  # put what you HAD into the room
                current_node.space_g = None  # clear the space for new stuff

# gloves increase damage
        except current_node.item_w or current_node.item_m or current_node.item_a or current_node.item_g or \
                current_node.item_h or current_node.item_k or current_node.item_s is None:
            print("There's nothing to PICK UP here silly.")

    if command == "drop magic":
        try:
            inventory.magic = None
            current_node.item_m.append = inventory.magic
            print("You dropped your %s." % inventory.magic)
        except inventory is None:
            print("Spongebob, you can't, you're nonexistent equipment can't go any lower than being your possession.")

    if command == "drop weapon":
        try:
            inventory.weapon = None
            current_node.item_w.append = inventory.weapon
            print("You dropped your %s." % inventory.weapon)
        except inventory is None:
            print("Spongebob, you can't, you're nonexistent equipment can't go any lower than being your possession.")

    if command == "drop armor":
        try:
            print("You dropped your %s." % inventory.armor)
            current_node.item_a.append = inventory.armor
            inventory.armor = None
        except inventory is None:
            print("Spongebob, you can't, you're nonexistent equipment can't go any lower than being your possession.")

    if command == "drop key":
        try:
            print("You dropped your %s." % inventory.key)
            current_node.item_k.append = inventory.key
            inventory.key = None
        except inventory is None:
            print("Spongebob, you can't, you're nonexistent equipment can't go any lower than being your possession.")

    if command == "drop heal":
        try:
            print("You dropped your %s." % inventory.heal)
            current_node.item_h.append = inventory.heal
            inventory.heal = None
        except inventory is None:
            print("Spongebob, you can't, you're nonexistent equipment can't go any lower than being your possession.")

#  Stupid Shiz
    if command == "think":
        print("You become a plagiarizer.")
# game over
    if Spongebob.lives <= 0:
        Spongebob.game_over()
        exit()

#  Easter eggs
#  Snap
#     if command == "snap":
#         try:
#              inventory.gloves(infinity_gauntlet)
#
#         except not inventory.gloves(infinity_gauntlet):
#     if command == "test":
#         Spongebob.xp += 10
