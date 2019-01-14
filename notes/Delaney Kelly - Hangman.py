import random
words = ["shouldn't", "dwarf", "elephant", "banjo", "pixel", "unzip", "don't", "green", "mystery",
         "bagpipes", "water"]

answer_word = random.choice(words)

answer_letters = list(answer_word)
blank_answer = []
guessed_letters = []
mistakes = 8

for item in answer_letters:  # Make _s for letters in a new list
    current_index = answer_letters.index(item)
    blank_answer.insert(current_index, "_ ")

if "'" in answer_letters:
    blank_answer[answer_letters.index("'")] = "'"

print('The answer is %d letters long' % len(answer_letters))
print("".join(blank_answer))  # print a joined list
guess = ""

while mistakes > 0:  # actually playing the game
    # Build blank_answer
    guessed_letters.append(guess)
    # Take input
    if blank_answer == answer_letters:  # won
        mistakes = 0
        print("Yay!, you won")
    elif mistakes == 0 and guess != answer_letters:  # lost
        print("You lost! ")  # switch won and lost?
    guess = input("Guess a letter: ")  # should go in the loop
    if guess in answer_letters and guess not in guessed_letters:
        guessed_letters.append(guess)
        blank_answer[answer_letters.index(guess)] = guess
        print("".join(blank_answer))

    elif guess not in answer_letters and guess not in guessed_letters:  # haven't guessed, not correct
        guessed_letters.append(guess)
        print("That letter is not in the word.")
    elif guess in guessed_letters:  # already guessed
        print("You have already guessed this letter.")

'''

    elif blank_answer == answer_letters:  # won
        mistakes = 0
        print("Yay! You won!")
        
    

you get 8 guesses
if guess == answer_letters:

if 'at' in listOfStrings :  # check if letter is in list

for character in answer_letters:
    if character(guess) == character(answer_letters):  # replace with a *
        current_index = words.index(character)
        answer_letters.pop(current_index)
        answer_letters.insert(current_index, "*")
        print(answer_letters)
'''
