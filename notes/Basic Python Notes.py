'''
print("Hello World!")
print()
This is a comment. I can write whatever I want
here and it won't do anything about it.
It has no effect on the code.
print()  # this adds extra spaces in the terminal
print("This will print here. Notice the spacing.")

a = 4
b = 3
print(a + b)
print(a * 5)
print(5 - 3)
print(6 / 5)  # results in a float (with decimals)

print("Figure this out")
print(6 // 4)
print(12 // 3)
print(9 // 4)  # results in an integer (without decimals)

MORE MATH STUFF

print(6 % 4)
print(5 % 3)
print(9 % 4)


# Variables
car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 1024
car_mph = 0.01

print("I have a car called %s. It's pretty nice." % car_name)

Input
name = input("What is your name? ")
print("Hello %s" % name)

auto comment - Ctrl + /
age = input("How old are you? ")
print("%s?! You belong in a museum." % age)

Hidden age
real_age = int(input("how old are you? >_"))
hidden_age = real_age + 5
print(hidden_age)
print("%d is incredibly old. You are actually %d years old" % (hidden_age, real_age))
'''

'''
This is a multi-line comment
I can type anywhere here
'''


# functions
def printHelloWorld():
    print("Hello World!")


printHelloWorld()

# f(x) = 2x + 3


def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)

# Loops
for i in (1, 2, 3):
    printHelloWorld()

print()
for i in range(3):
    printHelloWorld()

print()
for i in range(10):
    printHelloWorld()

print()
for i in range(5):  # Range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)


# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same thing as a = a + 1

'''
Hints with loops:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how may iterations
'''

# Random numbers
import random  # This should always be on line 1
print(random.randint(0, 100))


# Control statements
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(79))

# Equality statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)  # 3 is not equal to 4

# a = 3   means a is set to 3
# a == 3  asks is a equal to 3?

# Lists
shopping_list = ["Whole Milk", "Xbox One", "PC", "Eggs"]
print(shopping_list)  # prints whole list
print(shopping_list[0])  # prints first one
print("The second thing on the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a List
shopping_list[1] = "2% Milk"
print(shopping_list)
print(shopping_list[0])

# Looping Through Lists
for item in shopping_list:
    print(item)

christmas_list = ["Roller Skates", "Bike", "Toy Train", "Doll", "New Computer"]
christmas_list[2] = "Yo Yo"
print(christmas_list[2])
print(christmas_list)
print("The last thing in the list is %s" % christmas_list[len(christmas_list) - 1])

# Getting Part of a List
print(christmas_list[1:3])  # prints second and third item
print(christmas_list[1:4])  # prints second, third, and fourth item
print(christmas_list[1:])  # prints from second item to end

