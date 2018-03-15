world_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS': {
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'NORTHHOUSE': {
        'NAME': 'NORTH OF HOUSE',
        'DESCRIPTION': "You are west of a small house",
        'PATHS': {
            'WEST': "WESTHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'SOUTH OF PINEAPPLE',
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
        'PATHS': {
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTHHOUSE",
            'EAST': "EASTHOUSE"
        }
    }
}
current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
print(current_node)

while True:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized")
    print()


