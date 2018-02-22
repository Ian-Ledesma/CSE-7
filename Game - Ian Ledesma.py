Spongebob_Pineapple = {
    #SOUTH PINEAPPLE
    'EXTRM1': {
        'NAME': "SOUTH OF PINEAPPLE",
        'DESCRIPTION': "BEFORE YOU IS A MASSIVE METAL DOOR. NORTH OF YOU IS THE LIVING ROOM.",
        'PATHS': {
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'INTRM1': {
        'NAME': 'LIVING ROOM',
        'DESCRIPTION': "AHEAD OF YOU ARE TWO BALLOON SOFAS, 2 FISHHOOKS AND A PORTRAIT ON THE WALL, A HELMET FOR A TV,"
                       "AND A BLUE BAMBOO WALL. TO THE EAST IS A CLOSET, AND TO THE NORTH IS A KITCHEN.",
        'PATHS': {
            'SOUTH': "EXTRM1",
            'NORTH': "INTRM2"
        }
    },
    'INTRM2': {
        'NAME': 'KITHCEN',
        'DESCRIPTION': "THERE'S A KITHCEN WITH A METAL WALL TO ONE SIDE AND BOMBOO ON THE OTHER, AS WELL AS BAMBOO "
                       "CUBBOARDS AND SURF BOARD COUNTERS, AND A BUCKET FOR A SINK ",
        #FINISH THE DESCRIPTION
        'PATHS': {
            'SOUTH': "EXTRM1",
            'NORTH': "INTRM2"
        }
    },
    'INTRM3': {
        'NAME': 'KITHCEN WINDOW',
        'DESCRIPTION': "YOU LEAN ON A MATAL RIMMED, CIRCLE WINDOW. NORTH, OUTSIDE OF IT IS THE OUTDOORS.",
        'PATHS': {
            'NORTH': "EXTRM3",
            'SOUTH': "INTRM2"
         }
    },

    'INTRM4': {
        'NAME': 'CLOSET',
        'DESCRIPTION': "YOU SEE A COLLECTION OF PARTY SUPPLIES, COOKING SUPPLIES, AND OTHER SUPPLIES OF LITERALLY "
                       "ANYTHING ELSE. WE-A-ST OF YOU IS A SMALL DOOR, LEADING TO SOMEONE ELSE'S ROOM ...",
        'PATHS': {
            'WEST': "INTRM1",
            'EAST': "INTRM14"
        }
    },
    'INTRM5': {
        'NAME': "LADDER",
        'DESCRIPTION': "YOU'RE ON A BAMBOO LADDER, WITH THE ONLY PLACES TO GO BEING UP OR DOWN.",
        'PATHS': {
            'UP': "INTRM6",
            'DOWN': "INTRM15",
            #CAN'T GO SOUTH TO GARY'S MIND
        }
    },
    'INTRM6': {
        'NAME': "BEDROOM",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': "INTRM8",
            'WEST': "INTRM9",
            'DOWN': "INTRM7",
            'UP': "INTRM16"
        }
    },
    'INTRM7': {
        'NAME': "LIBRARY",
        'DESCRIPTION': " ",
        'PATHS': {
            'UP': "INTRM6"
        }
    },
    'INTRM8': {
        'NAME': "BEDROOM WINDOW",
        'DESCRIPTION': "OUTSIDE OF THE WINDOW IS A STREET, SAND ON EITHER SIDE FOR AS AFAR AS THE EYE CAN SEE. NORTHWARD"
                       "IS A 2 STORY FALL TO THE OUTER WORLD",
        'PATHS': {
            'NORTH': "EXTRM4",
            'SOUTH': "INTRM6",
        }
    },
    'INTRM9': {
        'NAME': "HALLWAY",
        'DESCRIPTION': "YOU WALK THROUGH A GREEM FLORAL WALLED PATHWAY, WEST OF YOU BEING A RESTROOM",
        'PATHS': {
            'WEST': "INTRM10",
            'EAST': "INTRM6"
        }
    },
    'INTRM10': {
        'NAME': "RESTROOM",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': "INTRM11",
            'EAST': "INTRM9",
        }
    },
    'INTRM11': {
        'NAME': "RESTROOM WINDOW",
        'DESCRIPTION': "OUTSIDE OF THE WINDOW IS A SANDY FLOOR, WITH A CITY FAR OFF INTO THE DISTANCE."
                       "SOUTH IS A 2 STORY FALL TO THE OUTER WORLD",
        'PATHS': {
            'NORTH': "EXTRM3",
            'SOUTH': "INTRM10",
        }
    },
    'INTRM12': {
        'NAME': "KITCHEN WINDOW",
        'DESCRIPTION': "OUTSIDE OF THE WINDOW IS A STREET, SAND ON EITHER SIDE FOR AS AFAR AS THE EYE CAN SEE. "
                       "SOUTHWARD IS A 2 STORY FALL TO THE OUTER WORLD",
        'PATHS': {
            'SOUTH': "EXTRM1",
            'WEST': "INTRM2",
        }
    },
    'INTRM13': {
        'NAME': "GARAGE",
        'DESCRIPTION': "OUTSIDE OF THE WINDOW IS A STREET, SAND ON EITHER SIDE FOR AS AFAR AS THE EYE CAN SEE. "
                       "SOUTHWARD IS A 2 STORY FALL TO THE OUTER WORLD",
        'PATHS': {
            'EAST': "INTRM2",
            'WEST': "EXTRM2"
        }
    },
    'INTRM14': {
        'NAME': "GARY'S ROOM",
        'DESCRIPTION': "YOU SEE A PINK WALLED ROOM, WITH A DISPLAY OF A SNAIL SHELL, BUCKETS OF TOYS EVERYWHERE, AND "
                       "A GLORIOUS SNAIBED. AND TO THE WEST IS A BLUE SLUG, STARING INTO YOUR SOUL WITH A FEROCITY TO "
                       "SHAKE THE MOST ENDEAERING OF MEN. THE ONLY PATH FROM HERE BACK, BUT YOU SENSE YOUR SOUL BEING "
                       "PULLED EASTWARD, TO THE SNAIL.",
        'PATHS': {
            'EAST': "MAZE1",
            'WEST': "INTRM4"
        }
    },
    'INTRM15': {
        'NAME': "CELLAR",
        'DESCRIPTION': "YOU SEE MANY BARRELS FILLED WITH ROOT BEER, FROM FLOOR TO CEILING, WITH THE ONLY WAY OUT BEING"
                       "UP.",
        'PATHS': {
            'UP': "INTRM5"
        }
    },
    'INTRM16': {
        'NAME': "SUNROOF",
        'DESCRIPTION': "AROUND YOU ARE MASSIVE PINEAPPLE LEAVES, BUT A NAKED CEILING, ALLOWING FOR SUN TO SHINE ON YOU."
                       "ALL AROUND IS A PATH TO FREEDOM, OR A RETREAT DOWNWARD.",
        'PATHS': {
            'NORTH': "EXTRM3",
            'SOUTH': "EXTRM1",
            'EAST': "EXTRM4",
            #MAKE AN EAST OF HOUSE TOO
            'WEST': "EXTRM2",
            'DOWN': "INTRM6"
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

    'EXTRM2': {
        'NAME': "WEST OF PINEAPPLE",
        'DESCRIPTION': "TO YOUR EAST, IS A PINEAPPLE, WITH THE ENTRANCE TO THE SOUTH, AND TO THE WEST IS AN EASTER "
                       "ISLAND STATUE HEAD",
        'PATHS': {
            'SOUTH': "INTRM1"
            #  SQUIDWARD'S HOUSE
        }
    },
    'EXTRM3': {
        'NAME': "NORTH OF PINEAPPLE",
        'DESCRIPTION': "THERE IS SAND AS FAR AS THE EYE CAN SEE, WITH A CITY IN THE DISTANCE",
        'PATHS': {
            'SOUTH': "INTRM1"
            #  SQUIDWARD'S HOUSE
        }
    },
}


class (object):
    def __init__(self, north, east, south, west):
        self.north = "NORTH"
        self.east = "EAST"
        self.south = "SOUTH"
        self.west = "WEST"
        self.up = "UP"
        self.down = "DOWN"


    def paths (self):
        if input == "NORTH" :
            self.north = "NORTH"
        elif input == "EAST":
            self.east = "EAST"
        elif input == "SOUTH":
            self.south = "SOUTH"
        elif input == "WEST":
            self.west = "WEST"
        elif input == "UP":
            self.up = "UP"
        elif input == "DOWN":
            self.down = "DOWN"
 