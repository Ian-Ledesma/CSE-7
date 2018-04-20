spongebob_pineapple = {

   'intrm1': {
        'name': 'living room',
        'description': "ahead of you are two balloon sofas, 2 fishhooks and a portrait on the wall, a helmet for a tv,"
                       "and a blue bamboo wall. to the east is a closet, and to the north is a kitchen.",
        'paths': {
            'south': "extrm1",
            'north': "intrm2"
        }
    },
   'intrm2': {
        'name': 'kithcen',
        'description': "there's a kitchen with a metal wall to one side and bamboo on the other, as well as bamboo "
                       "cuboards and surf board counters, and a bucket for a sink ",
        #  finish the description
        'paths': {
            'south': "extrm1",
            'north': "intrm2"
        }
    },
   'intrm3': {
        'name': 'kithcen window',
        'description': "you lean on a matal rimmed, circle window. north, outside of it is the outdoors.",
        'paths': {
            'north': "extrm3",
            'south': "intrm2"
         }
    },

   'intrm4': {
        'name': 'closet',
        'description': "you see a collection of party supplies, cooking supplies, and other supplies of literally "
                       "anything else. we-a-st of you is a small door, leading to someone else's room ...",
        'paths': {
            'west': "intrm1",
            'east': "intrm14"
        }
    },
   'intrm5': {
        'name': "ladder",
        'description': "you're on a bamboo ladder, with the only places to go being up or down.",
        'paths': {
            'up': "intrm6",
            'down': "intrm15",
            #  can't go south to gary's mind
        }
    },
   'intrm6': {
        'name': "bedroom",
        'description': "",
        'paths': {
            'north': "intrm8",
            'west': "intrm9",
            'down': "intrm7",
            'up': "intrm16"
        }
    },
   'intrm7': {
        'name': "library",
        'description': " ",
        'paths': {
            'up': "intrm6"
        }
    },
   'intrm8': {
        'name': "bedroom window",
        'description': "outside of the window is a street, sand on either side for as afar as the eye can see. northward"
                       "is a 2 story fall to the outer world",
        'paths': {
            'north': "extrm4",
            'south': "intrm6",
        }
    },
   'intrm9': {
        'name': "hallway",
        'description': "you walk through a greem floral walled pathway, west of you being a restroom",
        'paths': {
            'west': "intrm10",
            'east': "intrm6"
        }
    },
   'intrm10': {
        'name': "restroom",
        'description': "",
        'paths': {
            'north': "intrm11",
            'east': "intrm9",
        }
    },
   'intrm11': {
        'name': "restroom window",
        'description': "outside of the window is a sandy floor, with a city far off into the distance."
                       "south is a 2 story fall to the outer world",
        'paths': {
            'north': "extrm3",
            'south': "intrm10",
        }
    },
   'intrm12': {
        'name': "kitchen window",
        'description': "outside of the window is a street, sand on either side for as afar as the eye can see. "
                       "southward is a 2 story fall to the outer world",
        'paths': {
            'south': "extrm1",
            'west': "intrm2",
        }
    },
   'intrm13': {
        'name': "garage",
        'description': "outside of the window is a street, sand on either side for as afar as the eye can see. "
                       "southward is a 2 story fall to the outer world",
        'paths': {
            'east': "intrm2",
            'west': "extrm2"
        }
    },
   'intrm14': {
        'name': "gary's room",
        'description': "you see a pink walled room, with a display of a snail shell, buckets of toys everywhere, and "
                       "a glorious snaibed. and to the west is a blue slug, staring into your soul with a ferocity to "
                       "shake the most endeaering of men. the only path from here back, but you sense your soul being "
                       "pulled eastward, to the snail.",
        'paths': {
            'east': "maze1",
            'west': "intrm4"
        }
    },
   'intrm15': {
        'name': "cellar",
        'description': "you see many barrels filled with root beer, from floor to ceiling, with the only way out being"
                       "up.",
        'paths': {
            'up': "intrm5"
        }
    },
   'intrm16': {
        'name': "sunroof",
        'description': "around you are massive pineapple leaves, but a naked ceiling, allowing for sun to shine on you."
                       "all around is a path to freedom, or a retreat downward.",
        'paths': {
            'north': "extrm3",
            'south': "extrm1",
            'east': "extrm4",
            #make an east of house too
            'west': "extrm2",
            'down': "intrm6"
        }
    },

# #MAZE 1
#        'MAZE1': {
#         'NAME': "GARRY'S CONSCIOUS",
#         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED EAST, YOUR SOUL   ",
#         'PATHS': {
#             'NORTH': "NORTHHOUSE"
#     #MAZE
#         }
#     },
#     'MAZE1': {
#         'NAME': "GARRY'S CONSCIOUS",
#         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
#         'PATHS': {
#             'NORTH': "NORTHHOUSE"
#             # MAZE
#         }
#     }, 'MAZE1': {
#         'NAME': "GARRY'S CONSCIOUS",
#         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
#         'PATHS': {
#             'NORTH': "NORTHHOUSE"
#     #MAZE
#         }
#     }, 'MAZE1': {
#         'NAME': "GARRY'S CONSCIOUS",
#         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
#         'PATHS': {
#             'NORTH': "NORTHHOUSE"
#     #MAZE
#         }
#     },
'extrm1': {
       'name': "south of pineapple",
       'description': "before you is a massive metal door. north of you is the living room.",
       'paths': {
            'north': "northhouse",
            'south': "southhouse",
            'east': "easthouse"
        }
    },
   'extrm2': {
        'name': "west of pineapple",
        'description': "to your east, is a pineapple, with the entrance to the south, and to the west is an easter "
                       "island statue head",
        'paths': {
            'south': "intrm1"
            #  squidward's house
        }
    },
   'extrm3': {
        'name': "north of pineapple",
        'description': "there is sand as far as the eye can see, with a city in the distance",
        'paths': {
            'south': "intrm1"
            #  squidward's house
        }
    },
}

current_node = spongebob_pineapple['extrm1']
directions = ['north', 'south', 'east', 'west']
print(current_node)


# class (object):
#     def __init__(self, north, east, south, west):
#         self.north = "north"
#         self.east = "east"
#         self.south = "south"
#         self.west = "west"
#         self.up = "up"
#         self.down = "down"
#
#
#     def paths (self):
#         if input == "north" :
#             self.north = "north"
#         elif input == "east":
#             self.east = "east"
#         elif input == "south":
#             self.south = "south"
#         elif input == "west":
#             self.west = "west"
#         elif input == "up":
#             self.up = "up"
#         elif input == "down":
#             self.down = "down"





