class Room(object):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.description = description


#  Rooms
candy_store = Room("The Sweet Tooth Candy Store",
                   None, None, "alley", "dumpsters_2", None, None, None, None,
                   "There is a shelf with boxes of ferrero rocher chocolates right"
                   "in front of you. They cost $18. You need to buy one. The door to "
                   "the main alley south of you but to the west is another door. ")
office_store = Room("Office Depot",
                    None, "dumpsters_2", "alley", "dumpsters", None, None, None, None,
                    "In front of you is a neatly stacked pile of boxes in all sizes. Large boxes are $6. "
                    "There is also a shelf of pens and pencils, but the pencils are all sold out. "
                    "You need to find a pencil somewhere else. The alley is to the South, behind you but there are"
                    "two more side doors. One is to the East and one is to the West. ")
stationary_store = Room("The Stationary Store", None, None, "gate_1", None, None, None, "alley", None,
                        "There is a big wooden barrel filled with yellow pencils. They cost $4 each. The door to the "
                        "alley is behind you, to the Southeast but there is another door to the South. ")
alley = Room("The Dark Alley",
             "office_store", None, "under_the_bridge", None, "candy_store", "stationary_store", None, None,
             "The entrance to under the bridge is south, behind you. In front of you, north, is a brick "
             "building with a sign that reads 'Office Depot'. To the left (northwest) is a stationary store. "
             "To the right (northeast) is a candy store. ")
