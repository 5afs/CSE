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
