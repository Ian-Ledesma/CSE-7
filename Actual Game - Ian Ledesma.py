class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


extrm1 = Room()
extrm2 = Room()
extrm3 = Room()
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None,
              "ahead of you are two balloon sofas, 2 fishhooks and a portrait on the wall, a"
              " helmet for a tv, and a blue bamboo wall. to the east is a closet, and to the north is a kitchen.")
intrm2 = Room('Kitchen', 'extrm1', 'intrm2', None, None, None, None, "there's a kitchen with a metal wall to one"
            "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a sink")
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a matal rimmed, circle window."
              "north, outside of it is the outdoors.")
intrm4 = Room('Closet', None, None, intrm1, intrm14, None, None, "you see a collection of party supplies, cooking "
            "supplies, and other supplies of literally anything else. we-a-st of you is a small door, leading to"
            "someone else's room ...")
intrm5 = Room
intrm6 = Room
intrm7 = Room
intrm8 = Room
intrm9 = Room
intrm10 = Room
intrm11 = Room
intrm12 = Room
intrm13 = Room
intrm14 = Room
intrm15 = Room
intrm16 = Room
extrm2 = Room
extrm3 = Room
while True:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        try:
            name_of_node = current_node['paths'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized")
    print()


