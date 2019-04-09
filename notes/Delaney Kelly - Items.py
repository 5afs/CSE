class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self, name, description):
        super(Key, self).__init__(name, description)


class FerreroRocher(Item):
    def __init__(self, name, description, price):
        super(FerreroRocher, self).__init__(name, description)
        self.price = price


class Pencil(Item):
    def __init__(self, name, description, price):
        super(Pencil, self).__init__(name, description)
        self.price = price


class Box(Item):
    def __init__(self, name, description, price):
        super(Box, self).__init__(name, description)
        self.price = price


class Money(Item):
    def __init__(self, name, description, worth):
        super(Money, self).__init__(name, description)
        self.worth = worth


class Coupon(Item):
    def __init__(self, name, description, worth):
        super(Coupon, self).__init__(name, description)
        self.worth = worth


class Food(Item):
    def __init__(self, name, description, type):
        super(Food, self).__init__(name, description)
        self.type = type


class Car(Item):
    def __init__(self, name, description, brand, type, fuel, year):
        super(Car, self).__init__(name, description)
        self.brand = brand
        self.type = type
        self.fuel = fuel
        self.year = year


class Pet(Item):
    def __init__(self, name, description, kind, age):
        super(Pet, self).__init__(name, description)
        self.kind = kind
        self.age = age


class Sweater(Item):
    def __init__(self, name, description, color, style, material):
        super(Sweater, self).__init__(name, description)
        self.color = color
        self.style = style
        self.material = material


class Monster(Item):
    def __init__(self, name, description, weapon):
        super(Monster, self).__init__(name, description)
        self.weapon = weapon


class Computer(Item):
    def __init__(self, name, description, price, brand, year):
        super(Computer, self).__init__(name, description)
        self.price = price
        self.brand = brand
        self.year = year


class Notebook(Item):
    def __init__(self, name, description, paper_count, paper_rule):
        super(Notebook, self).__init__(name, description)
        self.paper_count = paper_count
        self.paper_rule = paper_rule


class Clock(Item):
    def __init__(self, name, description, time):
        super(Clock, self).__init__(name, description)
        self.time = time


class Glasses(Item):
    def __init__(self, name, description, strength, color):
        super(Glasses, self).__init__(name, description)
        self.strength = strength
        self.color = color


park_keyring = Key("A keyring", "can be used to unlock the park gates.")
dump_keyring = Key("Keys to the dump", "can be used to unlock the dump gates.")
zoo_key = Key("Key to the zoo", "can unlock the zoo gate.")
mechanical_pencil = Pencil("A mechanical pencil", "it is plastic and has an eraser", 5)
number_2_pencil = Pencil("A Number 2 Pencil", "A thin, yellow, sharpened pencil with a pink eraser on one end.", 1)
box_of_chocolates = FerreroRocher("A box of chocolates", "a clear plastic box filled with twelve Ferrero Rocher "
                                                         "candies.", 12)
small_box = Box("A small box", "a very small cardboard box, about the size of a shoebox", 5)
regular_box = Box("A normal box", "a medium sized box, one side is missing", 7)
big_box = Box("A really bog box", "a person could definitely fit inside.", 10)
penny = Money("A copper penny", "is worth one cent.", 0.01)
quarter = Money("A quarter", "is worth twenty-five cents.", 0.25)
dollar_bill = Money("A dollar bill", "is worth one dollar.", 1)
five_dollar_bill = Money("A five dollar bill", "is worth five dollars.", 5)
candy_store_coupon = Coupon("A coupon to the candy store", "is worth two dollars in the Sweet Tooth Candy Store.", 2)
stationary_store_coupon = Coupon("A coupon to the stationary store", "is worth enough to get one free pencil from "
                                                                     "the stationary store.", 1)
