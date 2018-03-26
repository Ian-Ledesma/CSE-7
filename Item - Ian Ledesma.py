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
    def __init__(self, name, description, attack, sand, kitchen_appliance, magic):
        super(Weapons, self). __init__(name, description)
        self.sand = sand
        self.kitchen_appliance = kitchen_appliance
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


class Kitchen_Appliance(Weapons):
    def  __init__(self,  name, description, attack, sand, kitchen_appliance, magic, spatula, neptune_spatula,
                  hydrodynamic_spatula,le_spatula, ladle, spoon):
        super(kitchen_appliance, self). __init__(self, name, description, attack, sand, kitchen_appliance, magic)
        self.spatula = spatula
        self.neptune_spatula = neptune_spatula
        self.hydrodynamic_spatula = hydrodynamic_spatula
        self.le_spatula = le_spatula
        self.ladle = ladle
        self.spoon = spoon
#Done


class Armor(Items):
    def __init__(self,name, description, natural, applicable):
        super(Armor, self). __init__(name, description)
        self.natural = natural
        self.applicable = applicable
# Done


class Applicable(Armor):
    def __init__(self, name, description, natural, applicable, sea_urchin_spikes):
        super(Applicable, self). __init__(name, description, natural, applicable)
        self.sea_urchin_spikes = sea_urchin_spikes
#  Done


class Natural(Armor):
    def __init__(self, name, description, natural, applicable, sponge_absorbtion, fat_flabs, krab_shell, spikes):
        super(Natural, self).__init__(name, description, natural, applicable)
        self.sponge_absorbtion = sponge_absorbtion
        self.fat_flabs = fat_flabs
        self.krab_shell = krab_shell
        self.spikes = spikes
#  Done


class Spikes(Natural):
    def __init__(self, name, description, natural, applicable, sponge_abrasion, pufferfish_spikes):
        super(Natural, self).__init__(name, description, natural, applicable)
        self.sponge_abrasion = sponge_abrasion
        self. pufferfish_spikes = pufferfish_spikes
#  Done


class Heal(Items):
    def __init__(self, name, description, food, imagination):
        super(Heal, self). __init__(name, description)
        self.food = food
        self.imagination = imagination
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

sand = Weapons("Sand", "The grains of sand below your paramulation apendages are your weapon.", 2)
spatula = Weapons("Spatula", "The ultimate kitchen appliance is your weapon, the spatula.", 20)
neptune_spatula = Weapons("Neptune's Spatula", "The spatula indicating divine culinary potential is your weapon.", 55)
hydrodynamic_spatula = Weapons("Hydro-Dynamic Spatula", "A multi-use spatula with utilities such as triple action"
                               "cooking, a bright, blinking, red light, and more, it is fit for only the most masterful"
                               "of chef.", 20*3)
le_spatula = Weapons("Le Spatula", "A spatula so fancy and self absorbed, that it will not let you touch it or touch anything for that matter, unless you are literally the best chef in the world, wher it will be the most useful of tools."
#  Turn into a class for the either does takes away your health, or helps you a lot

#  name, description, attack, magic,, hydrodynamic_spatula,le_spatula, ladle, spoon):