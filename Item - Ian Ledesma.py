class Items(object):
    def __init__(self, name, weapons, key, armor, heal):
        self.name = name
        self.weapons = weapons
        self.key = key
        self.armor = armor
        self.heal = heal


class Key(Items):
    def __init__(self, time_machine, clarinet):
        self.time_machine = time_machine
        self.clarinet = clarinet


class Weapons(Items):
    def __init__(self, sand, kitchen_appliance, magic):
        self.sand = sand
        self.kitchen_appliance = kitchen_appliance
        self.magic = magic


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
        self.sea_urchin_spikes = sea_urchin_spikes



class Heal(Items):
    def __init__(self, food, imagination):
        self.food = food
        self.imagination = imagination


class food(Heal):
    def __init__(self, krabby_patty, filter_feed):
        self.krabby_patty = krabby_patty
        self.filter_feed = filter_feed
