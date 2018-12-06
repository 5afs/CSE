def challenge1(first_name, last_name):      # Write name backwards
    print(last_name, first_name)


challenge1("Delaney", "Kelly")


def challenge2(digit):      # Tell if number is even or odd
    if digit % 2 ==0:
        print("%d is even." % digit)
    else:
        print("%d is odd." % digit)


challenge2(7)


def challenge3(base, height):    # Calculate area of triangle
    area = (base * height) / 2
    print("If the base of a triangle is %d and the height is %d, then the area is approximately %d"
          % (base, height, area))


challenge3(3, 7)


def challenge4(number1):    # Tell if number is positive, negative, or 0
    if number1 > 0:
        print("%d is positive." % number1)
    elif number1 < 0:
        print("%d is not positive." % number1)
    else:
        print("%d is zero." % number1)


challenge4(1.78)


def challenge5(radius):     # Find area of circle w/ radius
    area = 3.14*radius**2
    print("If the radius is %d, the area is %d." % (radius, area))


challenge5(4)


def challenge6(radius):     # volume of a sphere
    volume = (4/3) * 3.14 * radius**3
    print("If the radius of a sphere is %d, then the volume is approximately %d" % (radius, volume))


challenge6(7)


def challenge7(n):      # Accepts an integer (n) and computes the value of n+nn+nnn
    n = n + n**2 + n**3
    print(n)


challenge7(2)


def challenge8(number):     # Tell if a number is w/in 150 of 2000 or 3000
    if 1850 <= number <= 2150:
        print("The number is within 150 of 2000. ")
    elif 2850 <= number <= 3150:
        print("The number is within 150 of 3000. ")
    else:
        print("The number is not within 150 of 2000 or 3000. ")


challenge8(2130)


def challenge9(letter):     # Tell if a letter is a vowel
    vowels = ["a", "e", "i", "o", "u", "y"]
    if letter == vowels:
        print("%s is a vowel." % letter)
    else:
        print("%s is not a vowel." % letter)


challenge9("t")


def challenge10(string):    # Tell if a string is numeric
    if string == str(string):
        print("%s is not a number." % string)
    elif string == int(string):
        print("%s is a number." % string)


challenge10("Cat")
