print("Today is Catherine's birthday. You need to get her a number 2 pencil so she can copy your homework, a box of \n"
      "chocolates for her to eat, and a large box for her to live in.\n"
      "")


class LockException(Exception):
    pass


class Room(object):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest, description,
                 objects=None, characters=None, visits=0):
        if objects is None:
            objects = []
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
        self.characters = characters
        self.objects = objects
        self.visits = visits


class Gate(Room):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest, description,
                 description_unlocked, unreachable, characters=None, objects=None, visits=0, locked=True):
        super(Gate, self).__init__(name, north, east, south, west, northeast, northwest, southeast, southwest,
                                   description, characters, objects, visits)
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
        self.description_unlocked = description_unlocked
        self.unreachable = unreachable  # rooms you can't get to if the gate is locked
        self.characters = characters
        self.objects = objects
        self.visits = visits
        self.locked = locked


class Character(object):
    def __init__(self, name, starting_point, description, inventory=None, wallet=0):
        if inventory is None:
            inventory = []
        self.name = name
        self.location = starting_point
        self.description = description
        self.inventory = inventory
        self.wallet = wallet

    def move(self, new_location):
        """ this method moves a character to a new location

        :param new_location: the variable containing a room object
        """
        self.location = new_location


#  Rooms
candy_store = Room("The Sweet Tooth Candy Store",
                   None, None, "alley", "dumpsters_2", None, None, None, None,
                   "There is a shelf with boxes of ferrero rocher chocolates right \n"
                   "in front of you. They cost $18. You need to buy one. The door to \n"
                   "the main alley south of you but to the west is another door. \n")

office_store = Room("Office Depot",
                    None, "dumpsters_2", "alley", "dumpsters", None, None, None, None,
                    "In front of you is a neatly stacked pile of boxes in all sizes. Large boxes are $6. \n"
                    "There is also a shelf of pens and pencils, but the pencils are all sold out. "
                    "You need to find a pencil somewhere else. The alley is to the South, behind you but there are \n"
                    "two more side doors. One is to the East and one is to the West. ")

stationary_store = Room("The Stationary Store",
                        None, None, "gate_1", None, None, None, "alley", None,
                        "There is a big wooden barrel filled with yellow pencils. They cost $4 each. The door to the \n"
                        "alley is behind you, to the Southeast but there is another door to the South. ")

alley = Room("The Dark Alley",
             "office_store", None, "under_the_bridge", None, "candy_store", "stationary_store", None, None,
             "The entrance to under the bridge is south, behind you. In front of you, north, is a brick \n"
             "building with a sign that reads 'Office Depot'. To the left (northwest) is a stationary store. \n"
             "To the right (northeast) is a candy store. ")

bridge = Room("The Bridge",
              None, "gate_2", None, "gate_1", None, None, None, None,
              "You are standing on top of a bridge. To the East is the East Park Gate and to the West is the \n"
              "West Park Gate. You can see an alley and a row of stores below you to the North, but you can't \n"
              "get to it from here. To the South the bridge overlooks a forest, a fountain, and even farther \n"
              "in the distance is a picnic area with rows of benches. ")

under_bridge = Room("Under The Bridge",
                    "alley", None, None, None, None, None, "fountain", "forest",
                    "You are underneath a brick bridge. To the North, it is dark and you can see a little bit of \n"
                    "glowing light. To the other side, there is a little more light coming in. To the Southeast you \n"
                    "can hear water falling. To the southwest, you can see some trees. ")

lemonade_stand = Room("The Lemonade Stand",
                      None, None, "zoo_gate", "gate_2", None, None, None, None,
                      "There is a little kids' lemonade stand with a pitcher of iced lemonade and a pile of empty \n"
                      "cups. Also on the table is a sign that says 'sorry! we are closed. come back later. Behind \n"
                      "the sign is a glass jar filed with money. You can't see anyone around you. To the south is \n"
                      "the gate to the zoo. To the West is the East Park Gate. ")

well = Room("A Well",
            "forest", "clearing", None, None, None, None, None, None,
            "You are in a small clearing. In the middle of the clearing is a well. There is a rope going \n"
            "into it and there is a bucket on the end. To the north, the path leads into the forest and to \n"
            "the East is another trail. ")

clearing = Room("A Clearing",
                "well", None, "gate_3", None, None, None, None, None,
                "You are in the middle of a clearing. There is an old no. 2 pencil on the ground. The trail \n"
                "leads into the forest to the north and the south. ")

benches = Room("The Picnic Area",
               "fountain", None, None, None, None, None, None, None,
               "You are in the middle of a group of picnic benches. There is a sleeping park guard on one of \n"
               "the benches. You can see his key ring on the bench behind him. To the north is a fountain. ")

fountain = Room("The Fountain",
                None, None, "benches", None, "gate_2", "under_bridge", None, None,
                "You are next to a fountain that is shooting water into a pool. There are hundreds of coins \n"
                "scattered in it. To the Northeast is the East Park Gate. To the South is a group of picnic \n"
                "benches. To the Northwest is an area under the bridge. ")

office = Room("The Dump's Office",
              "dump_gate", "trash_piles", "path_through_trash", None, None, None, None, None,
              "You are in the main dump office. There are piles of paper scattered on all the desks. You see \n"
              "a big cup of new yellow pencils. To the North is the main dump gate. To the East is a dense \n"
              "pile of trash that you can't get through but to the South is a gap that you can fit through. ")

office_2 = Room("An Office",
                "dump_gate_2", None, "path_through_trash", "trash_piles", None, None, None, None,
                "You are in a small office. It is empty and there are no office supplies. It looks deserted. \n"
                "To the North is the Second Dump Gate. To the West are piles of trash that you won't be able to \n"
                "walk through, but to the South is a narrow path between the piles of trash. ")

pile_of_trash = Room("The Middle of Many Piles of Trash",
                     None, "office", None, "office_2", None, None, None, None,
                     "You are in the middle of heaps of garbage. You can barely walk through them but to the East \n"
                     "is the main office and to the West is another, smaller, office. The doors to both offices are \n"
                     "unlocked. ")

west_of_cage = Room("West of the Monkey Cage",
                    None, None, "front_of_cage", None, "zoo_gate", None, None, None,
                    "You are on the West side of the monkey cage. To the Northeast is the gate to the zoo and to the \n"
                    "South is the front of the cage. ")

east_of_cage = Room("East of Monkey Cage",
                    "west_of_cage", "east_of_cage", None, None, None, None, None, None,
                    "You are on the East side of hte monkey cage. To the North is the gate to the zoo and to the \n"
                    "West is the front of the cage. ")

front_of_cage = Room("In Front of the Monkey Cage",
                     "west_of_cage", "east_of_cage", None, None, None, None, None, None,
                     "You are in front of the monkey cage. Catherine is here. To the North is the west side of the \n"
                     "monkey cage and to the East is the East side of the cage. ")

dumpsters = Room("A Side Alley", None, "office_store", None, "stationary_store", None, None, None, None,
                 "You are in a small side alley. There is an open dumpster in front of you. To the East and the \n"
                 "West are doors. ")

dumpsters_2 = Room("Another Side Alley",
                   None, "candy_store", None, "office_store", None, None, None, None,
                   "You are in a small side alley. There is an open dumpster in front of you. To the East and the \n"
                   "West are doors. ")

# Gates
gate_1 = Gate("The West Park Gate",
              "alley", "bridge", "dump_gate", None, None, None, "forest", None,
              "You are standing in front of a big iron gate. It is locked but through the bars you can see \n"
              "outside the park. To the North is the alley. To the South is \n"
              "the main gate to the city dump. Inside the park, to the East is a Bridge. To the Southeast is a dark \n"
              "forest and you can barely see a narrow dirt trail going into it. ",

              "You are standing in a big, unlocked, iron gate open to the park. To the South is \n"
              "the main gate to the city dump. Inside the park, to the East is a Bridge. To the Southeast is a dark \n"
              "forest and you can barely see a narrow dirt trail going into it.",
              ["alley", "dump_gate"],
              None, None, 0, True)

gate_2 = Gate("The East Park Gate",
              "alley", "lemonade_stand", None, "bridge", None, None, "zoo_gate", "fountain",
              "You are standing in front of a locked iron gate that leads to the park. In the park, to the \n"
              "West is a bridge and to the Southwest is a circular fountain that is shooting water into a \n"
              "large tile pool. To the North, through the park gate, is an alley. To the East \n"
              "is a lemonade stand. To the Southeast is the gate to the zoo. ",

              "You are standing in an open iron gate that leads to the park. In the park, to the \n"
              "West is a bridge and to the Southwest is a circular fountain that is shooting water into a \n"
              "large tile pool. To the North, not in the park, is the Sweet Tooth Candy Store. To the East \n"
              "is a lemonade stand. To the Southeast is the gate to the zoo.",
              ["alley", "lemonade_stand", "zoo_gate"],
              None, None, 0, True)

gate_3 = Gate("The South Park Gate",
              "clearing", "dump_gate_2", None, "dump_gate", None, None, None, None,
              "You are standing in front of a locked gate that leads into and out of the park. To the North is a \n"
              "thick forest but you can barely see a narrow path leading into it. To the West \n"
              "is is the main gate to the dump. You can see that it is unlocked. To the East is the second \n"
              "dump gate. ",

              "You are standing in front of an open gate that leads into and out of the park. To the North is a \n"
              "thick forest but you can barely see a narrow path leading into it. To the West \n"
              "is is the main gate to the dump. You can see that it is locked. To the East is the second \n"
              "dump gate. ",
              ["dump_gate", "dump_gate_2"],
              None, None, 0, False)

dump_gate = Gate("The First Dump Gate",
                 "gate_1", "gate_3", "office", None, None, None, None, None,
                 "You are in front of a locked gate with a sign that reads 'City Dump: Gate 1'. Inside the gate, \n"
                 "to the South, you can see an office. To the North is the West Park Gate and to the East is \n"
                 "the South Park Gate. ",

                 "You are in front of an unlocked gate with a sign that reads 'City Dump: Gate 1'. Inside the gate, \n"
                 "to the South, you can see an office. To the North is the West Park Gate and to the East is \n"
                 "the South Park Gate. ",
                 ["office"],
                 None, None, 0, False)

dump_gate_2 = Gate("The Second Dump Gate",
                   None, "zoo_gate", "office_2", "gate_3", None, None, None, None,
                   "You are standing in front of a locked gate that says 'City Dump: Gate 2'. To the South, inside \n"
                   "the gate, there is an empty office. To the East is the Zoo Gate. To the West is the South Park \n"
                   "Gate. ",

                   "You are standing in front of an unlocked gate that says 'City Dump: Gate 2'. To the South, \n"
                   "inside the gate, there is an empty office. To the East is the Zoo Gate. To the West is the South \n"
                   "Park Gate.",
                   ["office_2"],
                   None, None, 0, True)

zoo_gate = Gate("The Gate to the Zoo",
                "lemonade_stand", None, "east_of_cage", "dump_gate_2", None, "gate_2", None, "west_of_cage",
                "",
                "You are at the zoo gate. To the North is the Lemonade stand and to the Northwest is the South \n"
                "Park Gate. To the South and the Southwest you can walk around a large monkey cage. To the \n"
                "West is a gate to the city dump. ",
                ["east_of_cage", "west_of_cage"],
                None, None, 0, False)


class Item(object):
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description


class Key(Item):
    def __init__(self, name, location, description):
        super(Key, self).__init__(name, location, description)


class FerreroRocher(Item):
    def __init__(self, name, location, description, price):
        super(FerreroRocher, self).__init__(name, location, description)
        self.price = price


class Pencil(Item):
    def __init__(self, name, location, description, price):
        super(Pencil, self).__init__(name, location, description)
        self.price = price


class Box(Item):
    def __init__(self, name, location, description, price):
        super(Box, self).__init__(name, location, description)
        self.price = price


class Money(Item):
    def __init__(self, name, location, description, worth):
        super(Money, self).__init__(name, location, description)
        self.worth = worth


class Coupon(Item):
    def __init__(self, name, location, description, worth):
        super(Coupon, self).__init__(name, location, description)
        self.worth = worth


park_keyring = Key("park keyring", benches, "can be used to unlock the park gates.")
dump_key = Key("dump key", dumpsters_2, "can be used to unlock the dump gates.")
zoo_key = Key("zoo key", dumpsters, "can unlock the zoo gate.")
mechanical_pencil = Pencil("mechanical pencil", stationary_store, "it is plastic and has an eraser", 5)
number_2_pencil = Pencil("a number 2 pencil", stationary_store, "A thin, yellow, sharpened pencil with a pink eraser "
                                                                "on one end.", 1)
box_of_chocolates = FerreroRocher("box of chocolates", candy_store, "a clear plastic box filled with twelve Ferrero "
                                                                    "Rocher candies.", 12)
small_box = Box("small box", office_store, "a very small cardboard box, about the size of a shoebox", 5)
regular_box = Box("normal box", office_store, "a medium sized box, one side is missing", 7)
big_box = Box("big box", office_store, "a person could definitely fit inside.", 10)
penny = Money("penny", fountain, "is worth one cent.", 0.01)
quarter = Money("quarter", fountain, "is worth twenty-five cents.", 0.25)
dollar_bill = Money("dollar bill", clearing, "is worth one dollar.", 1)
five_dollar_bill = Money("five dollar bill", lemonade_stand, "is worth five dollars.", 5)
candy_store_coupon = Coupon("coupon to the candy store", office_2, "is worth two dollars in the Sweet Tooth Candy "
                                                                   "Store.", 2)
stationary_store_coupon = Coupon("coupon to the stationary store", office_2, "is worth enough to get one free pencil "
                                                                             "from the stationary store.", 1)

item_list = [park_keyring, dump_key, zoo_key, mechanical_pencil, number_2_pencil, box_of_chocolates, small_box,
             regular_box, big_box, penny, quarter, dollar_bill, five_dollar_bill, stationary_store_coupon,
             candy_store_coupon]

#  Characters
player = Character("You", "bridge", None, [])
catherine = Character("Catherine", "front_of_cage", None, [])
trash_guy = Character("A man", "pile_of_trash", "He is dressed in baggy clothes and riding a bicycle. In his bike "
                                                "basket is a bundle of no. 2 pencils.", [number_2_pencil,
                                                                                         number_2_pencil,
                                                                                         number_2_pencil])

player.location = bridge
playing = True
directions = ["north", "east", "south", "west", "northeast", "northwest", "southeast", "southwest"]

while playing:
    player.location.visits += 1
    if isinstance(player.location, Gate) and player.location.locked:
        print(player.location.name)
        print(player.location.description)
        print()

    elif isinstance(player.location, Gate) and not player.location.locked:
        print(player.location.name)
        print(player.location.description_unlocked)
        print()

    elif player.location.visits < 2:  # only printing location description if they've not been there twice before
        print(player.location.name)
        print(player.location.description)
        print()

    else:
        print(player.location.name)
        print()

    for item in item_list:  # adding item descriptions to room descriptions
        if item.location == player.location.name:
            player.location.description.append(item.description)
            continue

    command = input(">_")

    if command.lower() in ['q', 'quit' 'exit']:  # ending game
        print("You have ended the game.")
        playing = False

        continue

    elif command.lower() in directions:  # moving from room to room

        try:
            # command is 'north'
            room_name = getattr(player.location, command)
            room_object = globals()[room_name]
            if isinstance(player.location, Gate):
                if room_name in player.location.unreachable:
                    raise LockException
            player.move(room_object)

        except KeyError:
            print("You are not able to go that way.")
            print()

        except LockException:
            print("The gate is locked. You cannot go through.")
            print()

    elif command == "look":
        print(player.location.description)
        print()

    elif "pick up" or "get" in command.lower():  # get object out of command
        command = command.replace("pick up ", "")
        # Search for matching item
        found_item = None

        for item in item_list:
            if item.name == command and item.location == player.location:
                found_item = item

        if found_item is None:
            print("There is no %s in this room" % command)

        elif isinstance(found_item, Money):
            player.inventory.append(found_item)
            player.wallet += found_item.worth
            found_item.location = player.inventory
            print("You have %s" % found_item.name)
            print("You have $%d." % player.wallet)

        else:
            player.inventory.append(found_item)
            found_item.location = player.inventory
            print("You have a %s" % found_item.name)

    else:
        print("Command Not Recognized")
        print()
