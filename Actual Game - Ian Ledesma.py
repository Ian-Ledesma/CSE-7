# Temporary Value
current_node = None


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


#  Defining a class
class Character(object):
    # TWO underscores before and after
    def __init__(self, state, name, description, inventory, item, attack, health, stats):
        #  Things that a Cat has
        self.state = state
        self.name = name
        self.description = description
        self.inventory = inventory
        self.item = item

        print("Oof. You Died.")


extrm1 = Room('South of Pineapple', 'intrm1', "#road", None, 'extrm2', None, None, "You're near a big metal door on a"
              "pine apple.\n North is a living room, south is a road, east is sand, and west is a window into "
              "Squidward's house.")
extrm2 = Room('West of Pineapple', None, "#road", "intrm13", "#Squidward's house", None, None, "" )
extrm3 = Room("North of Pineapple", None, 'extrm4', None, None, None, None, "Around you is sand, all but the window "
              "southward.")
extrm4 = Room()
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None, "In front of you is a room lined with fishing "
              "and swimming equipment as furniture, helmet for a tv, and a blue bamboo wall.\n To the east is a closet,"
              "and to the north is a kitchen.")
intrm2 = Room('Kitchen', 'extrm1', 'intrm2', None, None, None, None, "there's a kitchen with a metal wall to one"
              "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a "
              "sink")
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a metal rimmed, circle window."
              "north, outside of it is the outdoors.")
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "There's a collection of supplies for literally"
              "every scenario.\n East is the living room, and West is "
              "someone else's room ...")
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "You're on a bamboo ladder, "
              "\n with the only places "
              "to go being up or down.")
intrm6 = Room('Bedroom', "intrm8", None, "#hallway", None, None, "intrm7", "The room has red bamboo wallpaper on the "
              "right side and blue metal wallpaper on the left.")
intrm7 = Room('Library', None, None, None, None, 'intrm6', None, "All around you are books, and a recliner in the "
              "middle of it all.")
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
              "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world")
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "you walk o" )
intrm10 = Room('Restroom', 'intrm11', None, 'Intrm9', None, None,   )
intrm11 = Room('Restroom Window', 'extrm3', 'intrm10', None, None, None, None, "outside of the window is a sandy floor,"
               "with a city far off into the distance south is a 2 story fall to the outer world")
intrm12 = Room('Kitchen Window', None, 'extrm1', None, "intrm10", None, None, "outside of the window is a street, sand"
               " on either side for as afar as the eye can see. Southward is a 2 story fall to the outer world.")
intrm13 = Room('Garage', None, None, 'intrm2', 'extrm2', None, None, "A metal walled room, with tools one one of them"
               "and a large, mobile door.\n Westward is the outdoors, astward is a return to the   ")
intrm14 = Room("Gary's Mind", )
intrm15 = Room
intrm16 = Room()

#  Maze Gary
maze1 = Room("Gary's Mind", None, None, None, "maze2", None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze2 = Room("GAry's Mind", None, "maze3", None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze3 = Room("GaRy's Mind", None, None, "maze4", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze4 = Room("GarY's Mind", None, None, "maze5", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze5 = Room("Gary'S Mind", None, "maze6", None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze6 = Room("Gary's MInd", "maze7", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze7 = Room("Gary's MiNd", None, None, None, None, None, "maze8", "A disgustingly colorful expansion surrounds"
             " you.")
maze8 = Room("Gary's MinD", "intrm5", None, None, None, None, None, "A dark void surrounds you.\n but North is a"
             "brilliant light of ignorance and stupidity, in this void of acknowledgement and intelligence.")
#  Maze Spongebob
maze9 = Room("Spongebob's Mind", "maze10", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.")
maze10 = Room("SPongebob's Mind", None, "maze11", None, None, None, None, "A disgustingly colorful expansion surrounds"
              " you.")
maze11 = Room("SpOngebob's Mind", None, None, None, "maze12", None, None, "A disgustingly colorful expansion surrounds"
              " you.")
maze12 = Room("SpoNgebob's Mind", None, None, None, "maze13", None, None, "A disgustingly colorful expansion surrounds"
              " you.")
maze13 = Room("SponGebob's Mind", None, None, None, None, None, "maze14", "A disgustingly colorful expansion surrounds"
              " you.")
maze14 = Room("SpongEbob's Mind", None, None, None, None, "maze15", None, "A disgustingly colorful expansion surrounds"
              " you.")
maze15 = Room("SpongeBob's Mind", None, None, "maze16", None, None, None, "A disgustingly colorful expansion surrounds"
              " you.")
maze16 = Room("SpongebOb's Mind", None, None, None, None, None, "maze17", "A disgustingly colorful expansion surrounds"
              " you.")
maze17 = Room("SpongeboB's Mind", None, None, None, None, "maze18", None, "A disgustingly colorful expansion surrounds"
              " you.")
maze18 = Room("Spongebob'S Mind", None, None, None, None, None, "extrm2", "A disgustingly colorful expansion surrounds"
              " you.\n But above is relative darkness to this terrifying realm.")


current_node = extrm1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

# Controller
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        #  Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized")
        print("Oof big gays")
