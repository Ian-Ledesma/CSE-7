class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

#  Done


class Key(Items):
    def __init__(self, name, description, time_machine, clarinet, horse_radish):
        super(Key, self).__init__(name, description)
        self.time_machine = time_machine
        self.clarinet = clarinet
        self.horse_radish = horse_radish
#  Done

    def open(self):
        self.state == "unlock"  # Defined in character
#  Key Done


class Weapons(Items):
    def __init__(self, name, description, attack, sand, magic):
        super(Weapons, self). __init__(name, description)
        self.sand = sand
        self.magic = magic
        self.attack = attack
#  Done


class Magic(Weapons):
    def __init__(self, name, description, attack, sand, kitchen_appliance, magic, wand, hocus_pocus_kit, magic_conch,
                 imagination_box):
        super(Magic, self). __init__(name, description, attack, sand, kitchen_appliance, magic,)
        self.wand = wand
        self.hocus_pocus_kit = hocus_pocus_kit
        self.magic_conch = magic_conch
        self.imagination_box = imagination_box
#  Done Magic


class Kitchen_Appliance (Weapons):
    def __init__(self,  name, description, attack, sand, magic, spatula, neptune_spatula,
                 hydrodynamic_spatula, le_spatula, ladle, spoon):
        super(kitchen_appliance, self). __init__(self, name, description, attack, sand, kitchen_appliance, magic)
        self.spatula = spatula
        self.neptune_spatula = neptune_spatula
        self.hydrodynamic_spatula = hydrodynamic_spatula
        self.le_spatula = le_spatula
        self.ladle = ladle
        self.spoon = spoon
#  Done


class Armor(Items):
    def __init__(self, name, description, defense, damage_taken, natural, applicable):
        super(Armor, self). __init__(name, description)
        self.natural = natural
        self.applicable = applicable
        self.defense = defense
        self.damage_taken = damage_taken
# Done


class Applicable(Armor):
    def __init__(self, name, description, defense, damage_taken, natural, applicable, sea_urchin_spikes, metal):
        super(Applicable, self). __init__(name, description, defense, damage_taken, natural, applicable)
        self.sea_urchin_spikes = sea_urchin_spikes
        self.metal = metal
#  Done


class Natural(Armor):
    def __init__(self, name, description, defense, natural, applicable, sponge_absorbtion, fat_flabs,
                 krab_shell, spikes):
        super(Natural, self).__init__(name, description, defense, natural, applicable)
        self.sponge_absorbtion = sponge_absorbtion
        self.fat_flabs = fat_flabs
        self.krab_shell = krab_shell
        self.spikes = spikes
#  Done


class Spikes(Natural):
    def __init__(self, name, description, defense, damage_taken, natural, applicable, sponge_abrasion, pufferfish_spikes):
        super(Natural, self).__init__(name, description, defense, damage_taken, natural, applicable)
        self.sponge_abrasion = sponge_abrasion
        self. pufferfish_spikes = pufferfish_spikes
#  Done


class Heal(Items):
    def __init__(self, name, description, food, imagination):
        super(Heal, self). __init__(name, description)
        self.food = food
        self.imagination = imagination
        self.state == "Eating"  # Defined in character
# Done


class Food(Heal):
    def __init__(self, name, description, food, imagination, krabby_patty, filter_feed, mayo):
        super(Food, self). __init__(name, description, food, imagination)
        self.krabby_patty = krabby_patty
        self.filter_feed = filter_feed
        self.mayo = mayo
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
le_spatula = Weapons("Le Spatula", "A spatula so full of itself that it'll hurt YOU, unless you're a fanciful character")
#  Turn into a class for the either does takes away your health, or helps you a lot

#  magic
wand = Magic("Magic", "A black stick and star on the tip is your weapon.", 15)
hocus_pocus_kit = Magic("Mr.Magic's Magical Kit", "This kit includes a Book of Spells, a Wand of Whimsy, the beard of"
                        " Rasputin, and a license to practice magic. It possesses the ability to turn anything into"
                        "mayonaise", 90)
magic_conch = Magic("Magic Conch", "This conch gives you the ultimate advice, telling you how to knock out an enemy "
                                   "in one hit.", 9999)
imagination_box = Magic("Imagination Box", "This box gives you as much power as you give it. In this case only 50.", 50)

#  armor
sea_urchin_spikes = Applicable("Sea Urchin Spikes", "A set of spikes for both protection and defense.", 4, 10)
metal = Applicable("Anti-Rust Metal", "Just some metal that doesn't rust", 2, 0)
sponge_absorbtion = Natural("Spongebob's Sponginess", "Spongebob's sponginess reduces damage dealt.", 1)
fat_flabs = Natural("Patrick's Fat", "Patrick's fat protects him.", 2)
krab_shell = Natural("Mr.Krabbs' Shell", "Mr. Krabb's shell protects his soft innards.", 10)
sponge_abrasion = Spikes("Spongebob's Abrasive Side", "Spongebob's abrasive side barks and bites", -2, 11)
pufferfish_spikes = Spikes("Mrs. Puff's Spikes", "In times of distress, Mrs. Puff's spikes inflate.", 3, 3)

#  Heal
Imagination = Heal("Imagination", "If you believe, you heal.")
Krabby_Patty = Food("Krabby Patty", "The ultimate food instils belief and health.")
Filter_Feed = Food("Filter Feed", "The water contains healing energies you can use")
