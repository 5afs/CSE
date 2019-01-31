world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Class",
        'DESCRIPTION': "The classroom you are in right now. There are two exits to the north side.",
        'PATHS': {
            'NORTH': 'PARKING_LOT'
        }
    },
    'PARKING_LOT': {
        'NAME': "The Parking Lot",
        'DESCRIPTION': "There are cars parked here. To the south in Mr. Wiebe's room.",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    }
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
