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


class Character(object):
    def __init__(self, name, starting_point, description):
        self.name = name
        self.location = starting_point
        self.description = description


#  Characters
self = Character("You", "bridge", None)
catherine = Character("Catherine", "front_of_cage", None)
trash_guy = Character("A man", "pile_of_trash", "He is dressed in baggy clothes and riding a bicycle. In his bike "
                                                "basket is a bundle of no. 2 pencils.")



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

stationary_store = Room("The Stationary Store",
                        None, None, "gate_1", None, None, None, "alley", None,
                        "There is a big wooden barrel filled with yellow pencils. They cost $4 each. The door to the "
                        "alley is behind you, to the Southeast but there is another door to the South. ")

alley = Room("The Dark Alley",
             "office_store", None, "under_the_bridge", None, "candy_store", "stationary_store", None, None,
             "The entrance to under the bridge is south, behind you. In front of you, north, is a brick "
             "building with a sign that reads 'Office Depot'. To the left (northwest) is a stationary store. "
             "To the right (northeast) is a candy store. ")

gate_1 = Room("The West Park Gate",
              "stationary_store", "bridge", "dump_gate", None, None, None, "forest", None,
              "You are standing in front of a big iron gate. It is locked but through the bars you can see"
              "inside the park. To the East is a Bridge. To the Southeast is a dark forest and you can barely"
              "see a narrow dirt trail going into it. To the North is the Stationary Store. To the South is "
              "the main gate to the city dump. ")

gate_2 = Room("The East Park Gate",
              "candy_store", "lemonade_stand", None, "bridge", None, None, "zoo_gate", "fountain",
              "You are standing in front of a locked iron gate that leads to the park. In the park, to the"
              "West is a bridge and to the Southwest is a circular fountain that is shooting water into a"
              "large tile pool. To the North, not in the park, is the Sweet Tooth Candy Store. To the East"
              "is a lemonade stand. To the Southeast is the gate to the zoo. ")

gate_3 = Room("The South Park Gate",
              "clearing", "dump_gate_2", None, "dump_gate", None, None, None, None,
              "You are standing in front of an open gate that leads into the park. Through the gate, you can"
              "only see a thick forest but there is a narrow path winding North, into the forest. To the West"
              "is is the main gate to the dump. You can see that it is locked. To the East is the second "
              "dump gate. ")

bridge = Room("The Bridge",
              None, "gate_2", None, "gate_1", None, None, None, None,
              "You are standing on top of a bridge. To the East is the East Park Gate and to the West is the"
              "West Park Gate. You can see an alley and a row of stores below you to the North, but you can't"
              "get to it from here. To the South the bridge overlooks a forest, a fountain, and even farther"
              "in the distance is a picnic area with rows of benches. ")

under_bridge = Room("Under The Bridge",
                    "alley", None, None, None, None, None, "fountain", "forest",
                    "You are underneath a brick bridge. To the North, it is dark and you can see a little bit of"
                    "glowing light. To the other side, there is a little more light coming in. To the Southeast you"
                    "can hear water falling. To the southwest, you can see some trees. ")

lemonade_stand = Room("The Lemonade Stand",
                      None, None, "zoo_gate", "gate_2", None, None, None, None,
                      "There is a little kids' lemonade stand with a pitcher of iced lemonade and a pile of empty "
                      "cups. Also on the table is a sign that says 'sorry! we are closed. come back later. Behind"
                      "the sign is a glass jar filed with money. You can't see anyone around you. To the south is the"
                      "gate to the zoo. To the West is the East Park Gate. ")

well = Room("A Well",
            "forest", "clearing", None, None, None, None, None, None,
            "You are in a small clearing. In the middle of the clearing is a well. There is a rope going"
            "into it and there is a bucket on the end. To the north, the path leads into the forest and to"
            "the East is another trail. ")

clearing = Room("A Clearing",
                "well", None, "gate_3", None, None, None, None, None,
                "You are in the middle of a clearing. There is an old no. 2 pencil on the ground. The trail"
                "leads into the forest to the north and the south. ")

benches = Room("The Picnic Area",
               "fountain", None, None, None, None, None, None, None,
               "You are in the middle of a group of picnic benches. There is a sleeping park guard on one of"
               "the benches. You can see his key ring on the bench behind him. To the north is a fountain. ")

fountain = Room("The Fountain",
                None, None, "benches", None, "gate_2", "under_bridge", None, None,
                "You are next to a fountain that is shooting water into a pool. There are hundreds of coins "
                "scattered in it. To the Northeast is the East Park Gate. To the South is a group of picnic"
                "benches. To the Northwest is an area under the bridge. ")

dump_gate = Room("The First Dump Gate",
                 "gate_1", "gate_3", "office", None, None, None, None, None,
                 "You are in front of a locked gate with a sign that reads 'City Dump: Gate 1'. Inside the gate,"
                 "to the South, you can see an office. To the North is the West Park Gate and to the East is"
                 "the South Park Gate. ")

dump_gate_2 = ("The Second Dump Gate",
               None, "zoo_gate", "office_2", "gate_3", None, None, None, None,
               "You are standing in front of a locked gate that says 'City Dump: Gate 2'. To the South, inside"
               "the gate, there is an empty office. To the East is the Zoo Gate. To the West is the South Park"
               "Gate. ")

office = Room("The Dump's Office",
              "dump_gate", "trash_piles", "path_through_trash", None, None, None, None, None,
              "You are in the main dump office. There are piles of paper scattered on all the desks. You see"
              "a big cup of new yellow pencils. To the North is the main dump gate. To the East is a dense"
              "pile of trash that you can't get through but to the South is a gap that you can fit through. ")

office_2 = Room("An Office",
                "dump_gate_2", None, "path_through_trash", "trash_piles", None, None, None, None,
                "You are in a small office. It is empty and there are no office supplies. It looks deserted."
                "To the North is the Second Dump Gate. To the West are piles of trash that you won't be able to"
                "walk through, but to the South is a narrow path between the piles of trash. ")

pile_of_trash = Room("The Middle of Many Piles of Trash",
                     None, "office", None, "office_2", None, None, None, None,
                     "You are in the middle of heaps of garbage. You can barely walk through them but to the East"
                     "is the main office and to the West is another, smaller, office. The doors to both offices are"
                     "unlocked. ")

zoo_gate = Room("The Gate to the Zoo",
                "lemonade_stand", None, "east_of_cage", "dump_gate_2", None, "gate_2", None, "west_of_cage",
                "You are at the zoo gate. To the North is the Lemonade stand and to the Northwest is the South"
                "Park Gate. To the South and the Southwest you can walk around a large monkey cage. To the"
                "West is a gate to the city dump. ")

west_of_cage = Room("West of the Monkey Cage",
                    None, None, "front_of_cage", None, "zoo_gate", None, None, None,
                    "You are on the West side of hte monkey cage. To the Northeast is the gate to the zoo and to the"
                    "South is the front of the cage. ")

east_of_cage = Room("East of Monkey Cage",
                    "west_of_cage", "east_of_cage", None, None, None, None, None, None,
                    "You are on the East side of hte monkey cage. To the North is the gate to the zoo and to the"
                    "West is the front of the cage. ")

front_of_cage = Room("In Front of the Monkey Cage",
                     "west_of_cage", "east_of_cage", None, None, None, None, None, None,
                     "You are in front of the monkey cage. Catherine is here. To the North is the west side of the"
                     "monkey cage and to the East is the East side of the cage. ")

dumpsters = Room("A Side Alley", None, "office_store", None, "stationary_store", None, None, None, None,
                 "You are in a small side alley. There is an open dumpster in front of you. To the East and the"
                 "West are doors. ")

dumpsters_2 = Room("Another Side Alley",
                   None, "candy_store", None, "office_store", None, None, None, None,
                   "You are in a small side alley. There is an open dumpster in front of you. To the East and the"
                   "West are doors. ")
