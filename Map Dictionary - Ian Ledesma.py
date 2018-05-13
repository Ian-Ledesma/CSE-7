# spongebob_pineapple = {
#
#    'intrm1': {
#         'name': 'living room',
#         'description': "ahead of you are two balloon sofas, 2 fishhooks and a portrait on the wall, a helmet for a tv,"
#                        "and a blue bamboo wall. to the east is a closet, and to the north is a kitchen.",
#         'paths': {
#             'south': "extrm1",
#             'north': "intrm2"
#         }
#     },
#    'intrm2': {
#         'name': 'kithcen',
#         'description': "there's a kitchen with a metal wall to one side and bamboo on the other, as well as bamboo "
#                        "cuboards and surf board counters, and a bucket for a sink ",
#         #  finish the description
#         'paths': {
#             'south': "extrm1",
#             'north': "intrm2"
#         }
#     },
#    'intrm3': {
#         'name': 'kithcen window',
#         'description': "you lean on a matal rimmed, circle window. north, outside of it is the outdoors.",
#         'paths': {
#             'north': "extrm3",
#             'south': "intrm2"
#          }
#     },
#
#    'intrm4': {
#         'name': 'closet',
#         'description': "you see a collection of party supplies, cooking supplies, and other supplies of literally "
#                        "anything else. we-a-st of you is a small door, leading to someone else's room ...",
#         'paths': {
#             'west': "intrm1",
#             'east': "intrm14"
#         }
#     },
#    'intrm5': {
#         'name': "ladder",
#         'description': "you're on a bamboo ladder, with the only places to go being up or down.",
#         'paths': {
#             'up': "intrm6",
#             'down': "intrm15",
#             #  can't go south to gary's mind
#         }
#     },
#    'intrm6': {
#         'name': "bedroom",
#         'description': "",
#         'paths': {
#             'north': "intrm8",
#             'west': "intrm9",
#             'down': "intrm7",
#             'up': "intrm16"
#         }
#     },
#    'intrm7': {
#         'name': "library",
#         'description': " ",
#         'paths': {
#             'up': "intrm6"
#         }
#     },
#    'intrm8': {
#         'name': "bedroom window",
#         'description': "outside of the window is a street, sand on either side for as afar as the eye can see. northward"
#                        "is a 2 story fall to the outer world",
#         'paths': {
#             'north': "extrm4",
#             'south': "intrm6",
#         }
#     },
#    'intrm9': {
#         'name': "hallway",
#         'description': "you walk through a greem floral walled pathway, west of you being a restroom",
#         'paths': {
#             'west': "intrm10",
#             'east': "intrm6"
#         }
#     },
#    'intrm10': {
#         'name': "restroom",
#         'description': "",
#         'paths': {
#             'north': "intrm11",
#             'east': "intrm9",
#         }
#     },
#    'intrm11': {
#         'name': "restroom window",
#         'description': "outside of the window is a sandy floor, with a city far off into the distance."
#                        "south is a 2 story fall to the outer world",
#         'paths': {
#             'north': "extrm3",
#             'south': "intrm10",
#         }
#     },
#    'intrm12': {
#         'name': "kitchen window",
#         'description': "outside of the window is a street, sand on either side for as afar as the eye can see. "
#                        "southward is a 2 story fall to the outer world",
#         'paths': {
#             'south': "extrm1",
#             'west': "intrm2",
#         }
#     },
#    'intrm13': {
#         'name': "garage",
#         'description': "outside of the window is a street, sand on either side for as afar as the eye can see. "
#                        "southward is a 2 story fall to the outer world",
#         'paths': {
#             'east': "intrm2",
#             'west': "extrm2"
#         }
#     },
#    'intrm14': {
#         'name': "gary's room",
#         'description': "you see a pink walled room, with a display of a snail shell, buckets of toys everywhere, and "
#                        "a glorious snaibed. and to the west is a blue slug, staring into your soul with a ferocity to "
#                        "shake the most endeaering of men. the only path from here back, but you sense your soul being "
#                        "pulled eastward, to the snail.",
#         'paths': {
#             'east': "maze1",
#             'west': "intrm4"
#         }
#     },
#    'intrm15': {
#         'name': "cellar",
#         'description': "you see many barrels filled with root beer, from floor to ceiling, with the only way out being"
#                        "up.",
#         'paths': {
#             'up': "intrm5"
#         }
#     },
#    'intrm16': {
#         'name': "sunroof",
#         'description': "around you are massive pineapple leaves, but a naked ceiling, allowing for sun to shine on you."
#                        "all around is a path to freedom, or a retreat downward.",
#         'paths': {
#             'north': "extrm3",
#             'south': "extrm1",
#             'east': "extrm4",
#             #make an east of house too
#             'west': "extrm2",
#             'down': "intrm6"
#         }
#     },
#
# # #MAZE 1
# #        'MAZE1': {
# #         'NAME': "GARRY'S CONSCIOUS",
# #         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED EAST, YOUR SOUL   ",
# #         'PATHS': {
# #             'NORTH': "NORTHHOUSE"
# #     #MAZE
# #         }
# #     },
# #     'MAZE1': {
# #         'NAME': "GARRY'S CONSCIOUS",
# #         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
# #         'PATHS': {
# #             'NORTH': "NORTHHOUSE"
# #             # MAZE
# #         }
# #     }, 'MAZE1': {
# #         'NAME': "GARRY'S CONSCIOUS",
# #         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
# #         'PATHS': {
# #             'NORTH': "NORTHHOUSE"
# #     #MAZE
# #         }
# #     }, 'MAZE1': {
# #         'NAME': "GARRY'S CONSCIOUS",
# #         'DESCRIPTION': "AS YOU FEEL YOU FEEL YOUR SOUL BEING PULLED, YOU SEE A LIGHT NORTHWARD ",
# #         'PATHS': {
# #             'NORTH': "NORTHHOUSE"
# #     #MAZE
# #         }
# #     },
# 'extrm1': {
#        'name': "south of pineapple",
#        'description': "before you is a massive metal door. north of you is the living room.",
#        'paths': {
#             'north': "northhouse",
#             'south': "southhouse",
#             'east': "easthouse"
#         }
#     },
#    'extrm2': {
#         'name': "west of pineapple",
#         'description': "to your east, is a pineapple, with the entrance to the south, and to the west is an easter "
#                        "island statue head",
#         'paths': {
#             'south': "intrm1"
#             #  squidward's house
#         }
#     },
#    'extrm3': {
#         'name': "north of pineapple",
#         'description': "there is sand as far as the eye can see, with a city in the distance",
#         'paths': {
#             'south': "intrm1"
#             #  squidward's house
#         }
#     },
# }
#
# current_node = spongebob_pineapple['extrm1']
# directions = ['north', 'south', 'east', 'west']
# print(current_node)
#
#
# # class (object):
# #     def __init__(self, north, east, south, west):
# #         self.north = "north"
# #         self.east = "east"
# #         self.south = "south"
# #         self.west = "west"
# #         self.up = "up"
# #         self.down = "down"
# #
# #
# #     def paths (self):
# #         if input == "north" :
# #             self.north = "north"
# #         elif input == "east":
# #             self.east = "east"
# #         elif input == "south":
# #             self.south = "south"
# #         elif input == "west":
# #             self.west = "west"
# #         elif input == "up":
# #             self.up = "up"
# #         elif input == "down":
# #             self.down = "down"
#

extrm1 = Room('South of Pineapple', 'intrm1', None, None, 'extrm2', None, None, "You're near a big metal door on a"
              "pine apple.\n North is a living room, south is a road, east is sand, and west is a window into "
              "Squidward's house.", Plankton)
extrm2 = Room('West of Pineapple', None, None, "intrm13", None, None, None, "You're near a massive "
              "pineapple\n where eastward is back to the garage, westward is an easter-island-statue-house, and south "
              "is the road.", None)
#  make road and squidward's house later
extrm3 = Room("North of Pineapple", None, 'extrm4', None, None, None, None, "Around you is sand, all but the window "
              "southward.", None)
intrm1 = Room('Living Room', 'intrm2', 'extrm1', None, None, None, None, "In front of you is a room lined with fishing "
              "and swimming equipment as furniture, helmet for a tv, and a blue bamboo wall.\n To the east is a closet,"
              "and to the north is a kitchen.", None)
intrm2 = Room('Kitchen', 'extrm1', 'intrm2', None, None, None, None, "There's a kitchen with a metal wall to one"
              "side and bamboo on the other, as well as bamboo cuboards and surf board counters, and a bucket for a "
              "sink.\n Northward is the window, southward is the living room, eastward is another window, ", None)
intrm3 = Room('Kitchen Window', 'extrm3', 'intrm2', None, None, None, None, "you lean on a metal rimmed, circle window."
              "north, outside of it is the outdoors.", None)
intrm4 = Room('Closet', None, None, 'intrm1', 'intrm14', None, None, "There's a collection of supplies for literally"
              "every scenario.\n East is the living room, and West is "
              "someone else's room ...", None)
intrm5 = Room('Ladder', None, None, None, None, 'intrm6', 'intrm15', "You're on a bamboo ladder, "
              "\n with the only places "
              "to go being up or down.", None)
intrm6 = Room('Bedroom', "intrm8", None, "#hallway", None, None, "intrm7", "The room has red bamboo wallpaper on the "
              "right side and blue metal wallpaper on the left.", None)
intrm7 = Room('Library', None, None, None, None, 'intrm6', None, "All around you are books, and a recliner in the "
              "middle of it all.", None)
intrm8 = Room('Bedroom Window', 'extrm4', 'intrm6', None, None, None, None, "outside of the window is a street, sand" 
              "on either side for as afar as the eye can see. northward is a 2 story fall to the outer world", None)
intrm9 = Room('Hallway', None, None, "intrm6", "intrm10", None, None, "", None)
intrm10 = Room('Restroom', 'intrm11', None, 'intrm9', None, None, None, "Around you is a green, floral wall, with a tub"
               "toilet, sink, and a wringer.\n Northward is a window.", None)
intrm11 = Room('Restroom Window', 'extrm3', 'intrm10', None, None, None, None, "outside of the window is a sandy floor,"
               "with a city far off into the distance. \n South is a 2 story fall to the outer world", None)
intrm12 = Room('Kitchen Window', None, 'extrm1', None, "intrm10", None, None, "outside of the window is a street, sand"
               " on either side for as afar as the eye can see. Southward is a 2 story fall to the outer world.", None)
intrm13 = Room('Garage', None, None, 'intrm2', 'extrm2', None, None, "A metal walled room, with tools one one of them"
               "and a large, mobile door.\n Westward is the outdoors, eastward is a return to the hell of a demented "
               "mind.", None)
intrm14 = Room("Gary's Shell", None, None, "intrm4", "maze1", None, None, "You enter the pink snail shell and find a"
               "book shelf, a fire place, a recliner. \n Westward, toward the chair, is the snail with a gaze to shake "
               "the most mighty of warriors.", None)
intrm15 = Room("Cellar", None, None, None, None, "intrm 5", None, "You see many barrels filled with root beer, from "
               "floor to ceiling,\nwith the only way out being up.", None)
intrm16 = Room("Sunroof", "extrm3", "extrm1", None, "extrm2", None, "intrm6", "Around you are some big pineapple leaves"
               "and no ceiling.\n All around is a path to freedom, or a painful retreat downward.", None)
#  Maze Gary
maze1 = Room("Gary's Mind", None, None, None, "maze2", None, None, "A disgustingly colorful expansion surrounds"
             " you., None", None)
maze2 = Room("GAry's Mind", None, "maze3", None, None, None, None, "A disgustingly colorful expansion surrounds"
             "you.", None)
maze3 = Room("GaRy's Mind", None, None, "maze4", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze4 = Room("GarY's Mind", None, None, "maze5", None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze5 = Room("Gary'S Mind", None, "maze6", None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze6 = Room("Gary's MInd", "maze7", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze7 = Room("Gary's MiNd", None, None, None, None, None, "maze8", "A disgustingly colorful expansion surrounds"
             " you.", None)
maze8 = Room("Gary's MinD", "intrm5", None, None, None, None, None, "A dark void surrounds you.\n but North is a"
             "brilliant light of ignorance and stupidity, in this void of acknowledgement and intelligence.", None)
#  Maze Spongebob
maze9 = Room("Spongebob's Mind", "maze10", None, None, None, None, None, "A disgustingly colorful expansion surrounds"
             " you.", None)
maze10 = Room("SPongebob's Mind", None, "maze11", None, None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze11 = Room("SpOngebob's Mind", None, None, None, "maze12", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze12 = Room("SpoNgebob's Mind", None, None, None, "maze13", None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze13 = Room("SponGebob's Mind", None, None, None, None, None, "maze14", "A disgustingly colorful expansion surrounds"
              " you.", None)
maze14 = Room("SpongEbob's Mind", None, None, None, None, "maze15", None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze15 = Room("SpongeBob's Mind", None, None, "maze16", None, None, None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze16 = Room("SpongebOb's Mind", None, None, None, None, None, "maze17", "A disgustingly colorful expansion surrounds"
              " you.", None)
maze17 = Room("SpongeboB's Mind", None, None, None, None, "maze18", None, "A disgustingly colorful expansion surrounds"
              " you.", None)
maze18 = Room("Spongebob'S Mind", None, None, None, None, None, "extrm2", "A disgustingly colorful expansion surrounds"
              " you.\n But above is relative darkness to this terrifying realm.", None)