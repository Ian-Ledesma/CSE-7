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
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "you see a collection of party supplies, cooking "
            "supplies, and other supplies of literally anything else. we-a-st of you is a small door, leading to"
            "someone else's room ...")
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "you're on a bamboo ladder, with the only places "
              "to go being up or down." )
intrm6 = Room('Bedroom', )
#  do description
intrm7 = Room('Library', None, None, None, None, 'intrm6', None,
#  do description
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
            "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world")
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "you walk through a greem floral walled pathway, "
            "west of you being a restroom" )
intrm10 = Room
intrm11 = Room
intrm12 = Room
intrm13 = Room
intrm14 = Room
intrm15 = Room
intrm16 = Room

 current_node =
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    print(current_node ******)
    print(current_node ******)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        #  Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions [pos]
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        try:
            **********
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized")
    print()


