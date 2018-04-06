class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
#


class Key(Items):
    def __init__(self, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = False


class TimeMachine(Key):
    def __init__(self, name, description, allow_entry):
        super(TimeMachine, self). __init__(self, name, description)
        self.allow_entry = allow_entry


class Clarinet(Key):
    def __init__(self, name, description, allow_entry):
        super(Clarinet, self). __init__(self, name, description)
        self.allow_entry = allow_entry


class HorseRadish(Key):
    def __init__(self, name, description, allow_entry):
        super(TimeMachine, self). __init__(self, name, description)
        self.allow_entry = allow_entry

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
    def __init__(self, name, description, heal):
        super(Heal, self). __init__(name, description)
        self.heal = heal
        self.imagination = imagination
        self.krabby_patty = krabby_patty
        self.filter_feed = filter_feed
        self.mayo = mayo
        self.state = "Eating"
#  Done


'''
The items themselves 
'''

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
