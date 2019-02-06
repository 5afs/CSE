world_map = {
    'CANDY_STORE': {
        'NAME': "The Sweet Tooth Candy Store",
        'DESCRIPTION': "There is a shelf with boxes of ferrero rocher chocolates right in front of you. "
                       "They cost $18. You need to buy one. The door to the main alley south of you but to the west "
                       "is another door. ",
        'PATHS': {
            'SOUTH': 'ALLEY',
            'WEST': 'DUMPSTERS_2'
        }
    },
    'OFFICE_STORE': {
        'NAME': "Office Depot",
        'DESCRIPTION': "In front of you is a neatly stacked pile of boxes in all sizes. Large boxes are $6. "
                       "There is also a shelf of pens and pencils, but they are all out of pencils. "
                       "You need to find a pencil somewhere else. ",
        'PATHS': {
            'SOUTH': 'ALLEY'
        }
    },
    'STATIONARY_STORE': {
        'NAME': "The Stationary Store",
        'DESCRIPTION': "There is a big wooden barrel filled with yellow pencils. They cost $4 each. ",
        'PATHS': {
            'SOUTHEAST': 'ALLEY',
            'SOUTH': 'GATE_1'
        }
    },
    'ALLEY': {
        'NAME': "The dark alley",
        'DESCRIPTION': "The entrance to under the bridge is south, behind you. In front of you, north, is a brick "
                       "building with a sign that reads 'Office Depot'. To the left (northwest) is a stationary store. "
                       "To the right (northeast) is a candy store.  ",
        'PATHS': {
            'NORTH': 'OFFICE_STORE',
            'NORTHWEST': 'STATIONARY_STORE',
            'NORTHEAST': 'CANDY_STORE'
        }
    },
}


# Other Variables
current_node = world_map['R19A']  # starting room
directions = ["NORTH", "EAST", "SOUTH", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ['q', 'quit' 'exit']:
        playing = False
        continue
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("You can't go that way.")

    else:
        print("Command Not Recognized")
