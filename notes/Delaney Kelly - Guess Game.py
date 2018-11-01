import random
answer = random.randint(0, 10)


for i in (1, 2, 3, 4, 5):
    def guessing_correct(guess):
    if guess == answer:
        return "Correct!"
    elif guess > answer:
        return "Guess lower"
    elif guess < answer:
        return "Guess higher"




