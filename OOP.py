class Room(****):
    def __int__(self, name, north):
        self.name = name
        self.north = north

    def move(self, direction):
        global current_node
        current_node = globals()[getattr (self, direction)]

west_house = Room("West of House", 'north_house')
north_house = Room("North of House", None)