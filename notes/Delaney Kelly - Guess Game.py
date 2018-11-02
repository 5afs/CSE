import random
a = random.randint(1, 10)

for i in (1, 2, 3, 4, 5):
    g = int(input("You have five tries. Guess a number from one to ten: "))
    if g >= a:
        print("Guess lower: ")
    elif g <= a:
        print("Guess higher: ")
    elif g == a:
        print("You guessed it!")
    if i == 5:
        print("You lost :( ")

