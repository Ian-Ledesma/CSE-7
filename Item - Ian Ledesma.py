class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.weapons = weapons
        # self.key = key
        # self.armor = armor
        # self.heal = heal
#  Done


class Key(Items):
    def __init__(self, time_machine, clarinet, open):
        super(Key, self).__init__(self.name, self.description, time_machine, clarinet)
        self.time_machine = time_machine
        self.clarinet = clarinet
#  Key Done


class Weapons(Items):
    def __init__(self, sand, kitchen_appliance, magic):
        super(Weapons)
        self.sand = sand
        self.kitchen_appliance = kitchen_appliance
        self.magic = magic


class Magic(Weapons):
    def __init__(self, wand, hocus_pocus_kit, magic_conch, imagination_box):
        super(Magic, self). __init__(self.sand, self.kitchen_appliance, self.magic, self.wand, self.hocus_pocus_kit,
                                     self.magic_conch, self.imagination_box)
        self.wand = wand
        self.hocus_pocus_kit = hocus_pocus_kit
        self.magic_conch = magic_conch
        self.imagination_box = imagination_box
#  Done Magic

class Armor(Items):
    def __init__(self, natural, applicable):
        self.natural = natural
        self.applicable = applicable


class Natural(Armor):
    def __init__(self, sponge_absorbtion, fat_flabs, krab_shell, spikes):
        self.sponge_absorbtion = sponge_absorbtion
        self.fat_flabs = fat_flabs
        self.krab_shell = krab_shell
        self.spikes = spikes


class Spikes(Natural):
    def __init__(self, sponge_abrasion, sea_urchin_spikes, pufferfish_spikes):
        self.sponge_absorbtion = sponge_abrasion
        self. pufferfish = pufferfish_spikes


class Heal(Items):
    def __init__(self, food, imagination):
        self.food = food
        self.imagination = imagination


class food(Heal):
    def __init__(self, krabby_patty, filter_feed):
        self.krabby_patty = krabby_patty
        self.filter_feed = filter_feed
