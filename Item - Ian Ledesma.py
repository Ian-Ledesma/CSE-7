import random

while health >= 0 # define in character
    num = (random.randint(0, 101))

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
    def __init__(self, name, description, attack, rarity):
        super(Weapons, self). __init__(name, description, rarity)
        self.attack = attack


class LeSpatula(Weapons):
    def __init__(self, name, description, attack, rarity, self_harm):
        super(LeSpatula, self). __init__(name, description, attack, rarity)
        self.self_harm = self_harm
    if num > 20:
        self_harm = False
    else:
        self_harm = True

#Magic
class Magic(Weapons):
    def __init__(self, name, description, attack, rarity, mana_use):
        super(Magic, self). __init__(name, description, attack, rarity)
        self.mana_use = mana_use


class Armor(Items):
    def __init__(self, name, description, rarity, defense):
        super(Armor, self). __init__(name, description, rarity)
        self.defense = defense


class Spikes(Armor):
    def __init__(self, name, description, defense, rarity, attack):
        super(Spikes, self).__init__(name, description, rarity, defense)
        self.attack = attack


class Heal(Items):
    def __init__(self, name, description, rarity, heal):
        super(Heal, self). __init__(name, description, rarity)
        self.heal = heal
        self.state = "Eating"


'''
The items themselves 
'''

sand = Weapons("Sand", "The grains of sand below your perambulation appendages are your weapon.", 2, "Common")
spatula = Weapons("Spatula", "The ultimate kitchen appliance is your weapon, the spatula.", 20*3, "Uncommon")
neptune_spatula = Weapons("Neptune's Spatula", "The spatula indicating divine culinary potential is your weapon.", 55,
                          "Legendary")
hydrodynamic_spatula = Weapons("Hydro-Dynamic Spatula", "A multi-use spatula with utilities such as triple action" 
                               "cooking, a bright, blinking, red light, and more, it is fit for only the most masterful"
                               "of chef.", 20*3, "Legendary")
ladle = Weapons("Ladle", "A long, angled spoon is the pinnacle multi-utility, but for your use only a weapon", 20,
                "Rare")
spoon = Weapons("Spoon", "The average scoop.", 10, "Rare")
le_spatula = LeSpatula("Le Spatula", "A spatula so full of itself that it'll attack whoever sees fit.", 60, 20, "Epic")
#  magic
wand = Magic("Magic", "A black stick and star on the tip is your weapon.", 15, 10, "Common")
hocus_pocus_kit = Magic("Mr.Magic's Magical Kit", "This kit includes a Book of Spells, a Wand of Whimsy, the beard of"
                        " Rasputin, and a license to practice magic. It possesses the ability to turn anything into"
                        "mayonnaise", 45, 90, "Rare")
#  Be abl to transform enemy into mayo
magic_conch = Magic("Magic Conch", "This conch gives you the ultimate advice, telling you how to effectively knock out "
                    "an enemy", 9999, 9999, "Legendary")
imagination_box = Magic("Imagination Box", "This box gives you as much power as you give it. In this case only 50.", 50,
                        30, "Epic")
#  armor
sea_urchin_spikes = Spikes("Sea Urchin Spikes", "A set of spikes for both protection and defense.", 4, "Common", 10)
metal = Armor("Anti-Rust Metal", "Just some metal that doesn't rust", 5, "Uncommon")
sponge_absorbtion = Armor("Spongebob's Sponginess", "Spongebob's sponginess reduces damage dealt.", 20, "Legendary")
fat_flabs = Armor("Patrick's Fat", "Patrick's fat protects him.", 2, "Common")
krab_shell = Armor("Mr.Krabb's Shell", "Mr. Krabb's molted shell protects is an apt set of armor.", 10, None)
sponge_abrasion = Spikes("Spongebob's Abrasive Side", "Spongebob's abrasive side barks and bites", -2, 11, None)
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.", "Legendary", 20)
#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.", 10, None)
Krabby_Patty = Heal("Krabby Patty", "The ultimate food instills belief and health into the consumer.", 20)
Filter_Feed = Heal("Filter Feed", "The water contains healing energies you can use", 2, )
Mayo = Heal = ("Mayonnaise", "The ultimate substance, capable of preserving fish for eons.", 50, "Legendary")
