class Items(object):
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

#Key
class Key(Items):
    def __init__(self, name, description, rarity):
        super(Key, self).__init__(name, description, rarity)
        self.unlock = False


class TimeMachine(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(TimeMachine, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry


class Clarinet(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(Clarinet, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry

     def open(self, character):
         character.location = extrm1 #defined in room


class HorseRadish(Key):
    def __init__(self, name, description, rarity, allow_entry):
        super(HorseRadish, self). __init__(name, description, rarity)
        self.allow_entry = allow_entry

    def open(self):
        if self.unlock:
            print("U opened it lmao XD")
            self.unlock = True

#Weapons
class Weapons(Items):
    def __init__(self, name, description, rarity, strike):
        super(Weapons, self). __init__(name, description, rarity)
        self.strike = strike


class LeSpatula(Weapons):
    def __init__(self, name, description, rarity, strike, self_harm):
        super(LeSpatula, self). __init__(name, description, strike, rarity)
        self.self_harm = self_harm
    if num > 20:
        self_harm = False
    else:
        self_harm = True

#Magic
class Magic(Weapons):
    def __init__(self, name, description, rarity, strike, mana_use):
        super(Magic, self). __init__(name, description, strike, rarity)
        self.mana_use = mana_use

#Armor
class Armor(Items):
    def __init__(self, name, description, rarity, defense):
        super(Armor, self). __init__(name, description, rarity)
        self.defense = defense

#
class Spikes(Armor):
    def __init__(self, name, description, rarity, defense, strike):
        super(Spikes, self).__init__(name, description, rarity, defense)
        self.strike = strike

#Heal
class Heal(Items):
    def __init__(self, name, description, rarity, heal):
        super(Heal, self). __init__(name, description, rarity)
        self.heal = heal
        self.state = "Eating"

#Sock
class Socks(Items):
    def __init__(self, name, description, rarity, fall_soft):
        super(Socks, self). __init__(name, description, rarity)
        self.fall_soft = fall_soft

#Gloves
class Gloves(Items):
    def __init__(self, name, description, rarity, harder_hit):
        super(Gloves, self). __init__(name, description, rarity)
        self.harder_hit = harder_hit


attack = inventory.item_w.attack + inventory.item_g.harder_hit

"""
The items themselves 
"""

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
#  Be abl to transform enemy into mayo
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
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.", "Legendary", 20, 11)
#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.", "Rare", 10)
Krabby_Patty = Heal("Krabby Patty", "The ultimate food instills belief and health into the consumer.", "Epic", 20)
Filter_Feed = Heal("Filter Feed", "The water contains healing energies you can use", "Common",2 )
Mayo = Heal = ("Mayonnaise", "The ultimate substance, capable of preserving fish for eons.", 50, "Legendary")

#  Gloves
infinitegauntlet = Gloves("Infinty Gauntlet", )
