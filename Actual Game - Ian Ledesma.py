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


intrm1 = Room('living Room', 'intrm2', 'extrm1', None, None, None, None,
              "ahead of you are two balloon sofas, 2 fishhooks and a portrait on the wall, a"
              " helmet for a tv, and a blue bamboo wall. to the east is a closet, and to the north is a kitchen.")
extrm1 = Room

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


