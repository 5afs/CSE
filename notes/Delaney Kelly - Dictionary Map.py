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
                       "There is also a shelf of pens and pencils, but the pencils are all sold out. "
                       "You need to find a pencil somewhere else. The alley is to the South, behind you but there are"
                       "two more side doors. One is to the East and one is to the West. ",
        'PATHS': {
            'EAST': 'DUMPSTERS_2',
            'SOUTH': 'ALLEY',
            'WEST': 'DUMPSTERS'
        }
    },
    'STATIONARY_STORE': {
        'NAME': "The Stationary Store",
        'DESCRIPTION': "There is a big wooden barrel filled with yellow pencils. They cost $4 each. The door to the "
                       "alley is behind you, to the Southeast but there is another door to the South.",
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
            'NORTHEAST': 'CANDY_STORE',
            'SOUTH': 'UNDER THE BRIDGE',
            'NORTHWEST': 'STATIONARY_STORE'
        }
    },
    'GATE_1': {
        'NAME': "The West Park Gate",
        'DESCRIPTION': "You are standing in front of a big iron gate. It is locked but through the bars you can see"
                       "inside the park. To the East is a Bridge. To the Southeast is a dark forest and you can barely"
                       "see a narrow dirt trail going into it. To the North is the Stationary Store. To the South is "
                       "the main gate to the city dump. ",
        'PATHS': {
            'NORTH': 'STATIONARY_STORE',
            'EAST': 'BRIDGE',
            'SOUTHEAST': 'FOREST',
            'SOUTH': 'DUMP_GATE'
        }
    },
    'GATE_2': {
        'NAME': "The East Park Gate",
        'DESCRIPTION': "You are standing in front of a locked iron gate that leads to the park. In the park, to the"
                       "West is a bridge and to the Southwest is a circular fountain that is shooting water into a"
                       "large tile pool. To the North, not in the park, is the Sweet Tooth Candy Store. To the East"
                       "is a lemonade stand. To the Southeast is the gate to the zoo. ",
        'PATHS': {
            'NORTH': 'CANDY_STORE',
            'EAST': 'LEMONADE STAND',
            'SOUTHEAST': 'ZOO_GATE',
            'SOUTHWEST': 'FOUNTAIN',
            'WEST': 'BRIDGE'
        }
    },
    'GATE_3': {
        'NAME': "The South Park Gate",
        'DESCRIPTION': "You are standing in front of an open gate that leads into the park. Through the gate, you can"
                       "only see a thick forest but there is a narrow path winding North, into the forest. To the West"
                       "is is the main gate to the dump. You can see that it is locked. To the East is the second "
                       "dump gate. ",
        'PATHS': {
            'NORTH': 'CLEARING',
            'EAST': 'DUMP_GATE_2',
            'WEST': 'DUMP_GATE'
        }
    },
    'BRIDGE': {
        'NAME': "The Bridge",
        'DESCRIPTION': "You are standing on top of a bridge. To the East is the East Park Gate and to the West is the"
                       "West Park Gate. You can see an alley and a row of stores below you to the North, but you can't"
                       "get to it from here. To the South the bridge overlooks a forest, a fountain, and even farther"
                       "in the distance is a picnic area with rows of benches. ",
        'PATHS': {
            'EAST': 'GATE_2',
            'WEST': 'GATE_1'
        }
    },
    'UNDER_BRIDGE': {
        'NAME': "Under the Bridge",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'ALLEY',
            'SOUTHEAST': 'FOUNTAIN',
            'SOUTHWEST': 'FOREST'
        }
    },
    'LEMONADE_STAND': {
        'NAME': "The Lemonade Stand",
        'DESCRIPTION': " ",
        'PATHS': {
            'SOUTH': 'ZOO_GATE',
            'WEST': 'GATE_2'
        }
    },
    'WELL': {
        'NAME': "A Well",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'FOREST',
            'EAST': 'CLEARING'
        }
    },
    'CLEARING': {
        'NAME': "A clearing",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'WELL',
            'SOUTH': 'GATE_3'
        }
    },
    'BENCHES': {
        'NAME': "The picnic area",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'FOUNTAIN'
        }
    },
    'FOUNTAIN': {
        'NAME': "The Fountain",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTHEAST': 'GATE_2',
            'SOUTH': 'BENCHES',
            'NORTHWEST': 'UNDER_BRIDGE'
        }
    },
    'DUMP_GATE': {
        'NAME': "The First Dump Gate",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'GATE_1',
            'EAST': 'GATE_3',
            'SOUTH': 'OFFICE'
        }
    },
    'DUMP_GATE_2': {
        'NAME': "The Second Dump Gate",
        'DESCRIPTION': " ",
        'PATHS': {
            'EAST': 'ZOO_GATE',
            'SOUTH': 'OFFICE_2',
            'WEST': 'GATE_3'
        }
    },
    'OFFICE': {
        'NAME': "The dump's office",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'DUMP_GATE',
            'EAST': 'TRASH_PILES',
            'SOUTH': 'PATH_THROUGH_TRASH'
        }
    },
    'OFFICE_2': {
        'NAME': "An office",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'DUMP_GATE_2',
            'SOUTH': 'PATH_THROUGH_TRASH',
            'WEST': 'TRASH_PILES'
        }
    },
    'PILE_OF_TRASH': {
        'NAME': "The Middle of Many Piles of Trash",
        'DESCRIPTION': " ",
        'PATHS': {
            'EAST': 'OFFICE',
            'WEST': 'OFFICE_2'
        }
    },
    'ZOO_GATE': {
        'NAME': "The Gate to the Zoo",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'LEMONADE_STAND',
            'NORTHWEST': 'GATE_2',
            'SOUTH': 'EAST_OF_CAGE',
            'SOUTHWEST': 'WEST_OF_CAGE',
            'WEST': 'DUMP_GATE_2'
        }
    },
    'WEST_OF_CAGE': {
        'NAME': "West of the Monkey Cage",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTHEAST': 'ZOO_GATE',
            'SOUTH': 'FRONT_OF_CAGE'
        }
    },
    'EAST_OF_CAGE': {
        'NAME': "East of the Monkey Cage",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'ZOO_GATE',
            'WEST': 'FRONT_OF_CAGE'
        }
    },
    'FRONT_OF_CAGE': {
        'NAME': "In Front of the Monkey Cage",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'WEST_OF_CAGE',
            'EAST': 'EAST_OF_CAGE'
        }
    },
    'DUMPSTERS': {
        'NAME': "A Side Alley",
        'DESCRIPTION': " ",
        'PATHS': {
            'EAST': 'OFFICE_STORE',
            'WEST': 'STATIONARY_STORE'
        }
    },
    'DUMPSTERS_2': {
        'NAME': "A Side Alley",
        'DESCRIPTION': " ",
        'PATHS': {
            'EAST': 'CANDY_STORE',
            'WEST': 'OFFICE_STORE'
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
