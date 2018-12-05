def challenge1(first_name, last_name):
    print(last_name, first_name)


challenge1("Delaney", "Kelly")


def challenge5(radius):
    area = 3.14*radius**2
    print("If the radius is %d, the area is %d." % (radius, area))


challenge5(4)


def challenge8(number):
    if 1850 <= number <= 2150:
        print("The number is within 150 of 2000. ")
    elif 2850 <= number <= 3150:
        print("The number is within 150 of 3000. ")
    else:
        print("The number is not within 150 of 2000 or 3000. ")


challenge8(2130)


def challenge4(number1):
    if number1 > 0:
        print("%d is positive" % number1)
    elif number1 < 0:
        print("%d is not positive" % number1)
    else:
        print("%d is zero" % number1)


challenge4(1.78)


def challenge9(letter):
    vowels = ["a", "e", "i", "o", "u", "y"]
    if letter == vowels:
        print("%s is a vowel" % letter)
    else:
        print("%s is not a vowel" % letter)


challenge9("t")
