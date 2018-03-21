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
    def __init__(self, name, description, time_machine, clarinet, open):
        super(Key, self).__init__(name, description )
        self.time_machine = time_machine
        self.clarinet = clarinet
#  Key Done


class Weapons(Items):
    def __init__(self, name, description, sand, kitchen_appliance, magic):
        super(Weapons, self). __init__(name, description)
        self.sand = sand
        self.kitchen_appliance = kitchen_appliance
        self.magic = magic


class Magic(Weapons):
    def __init__(self, name, description, sand, kitchen_appliance, magic, wand, hocus_pocus_kit, magic_conch,
                 imagination_box):
        super(Magic, self). __init__(name, description, sand, kitchen_appliance, magic,)
        self.wand = wand
        self.hocus_pocus_kit = hocus_pocus_kit
        self.magic_conch = magic_conch
        self.imagination_box = imagination_box
#  Done Magic


class Armor(Items):
    def __init__(self,name, description, natural, applicable):
        super(Armor, self). __init__(name, description)
        self.natural = natural
        self.applicable = applicable


class Natural(Armor):
    def __init__(self, name, description, natural, applicable, sponge_absorbtion, fat_flabs, krab_shell, spikes):
        super(Natural, self).__init__(name, description, natural, applicable)
        self.sponge_absorbtion = sponge_absorbtion
        self.fat_flabs = fat_flabs
        self.krab_shell = krab_shell
        self.spikes = spikes


class Spikes(Natural):
    def __init__(self, name, description, natural, applicable, sponge_abrasion, pufferfish_spikes):
        super(Natural, self).__init__(name, description, natural, applicable)
        self.sponge_abrasion = sponge_abrasion
        self. pufferfish_spikes = pufferfish_spikes


class Heal(Items):
    def __init__(self, name, description, food, imagination):
        super(Heal, self). __init__(name, description)
        self.food = food
        self.imagination = imagination


class Food(Heal):
    def __init__(self, name, description, food, imagination, krabby_patty, filter_feed):
        super(Food, self). __init__(name, description, food, imagination)
        self.krabby_patty = krabby_patty
        self.filter_feed = filter_feed
