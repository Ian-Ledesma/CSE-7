world_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS':{
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'NORTHHOUSE': {
        'NAME': 'NORTH OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS':{
            'WEST': "WESTHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS': {
            'NORTH': "NORTHHOUSE",
            'WEST': "WESTHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'EASTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS':{
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }        
    },

    }
}

current_node = world_map['WESTHOUSE']
print(current_node["NAME"])
