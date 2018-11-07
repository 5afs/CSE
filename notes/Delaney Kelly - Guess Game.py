import random
win = False
a = random.randint(1, 10)
g = int(input("You have five tries. Guess a number from one to ten: "))
guesses_left = 5

while guesses_left > 0 and not win:
    if g == a:
        print("You Guessed It!")
        win = True
    elif g >= a:
        guesses_left -= 1
        g = int(input("Guess lower: "))
    elif g <= a:
        guesses_left -= 1
        g = int(input("Guess higher: "))
