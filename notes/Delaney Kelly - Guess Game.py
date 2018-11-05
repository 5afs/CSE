import random
a = random.randint(1, 10)
g = int(input("You have five tries. Guess a number from one to ten: "))

for i in (1, 2, 3, 4, 5):
    if g >= a:
        g = int(input("Guess lower: "))
    elif g <= a:
        print("Guess higher: ")
        g = int(input("Guess higher: "))
    elif g == a:
        print("You guessed it!")
    elif i == 5:
        print("You lost :( ")
