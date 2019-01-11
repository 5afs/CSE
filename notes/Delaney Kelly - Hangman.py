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

while mistakes > 0:  # actually playing the game
    guess = input("Guess a letter: ")  # should go in the loop
    if guess in answer_letters:
        mistakes -= 1
        guessed_letters.append(guess)
        blank_answer[answer_letters.index(guess)] = guess
        print("".join(blank_answer))
    elif guess in guessed_letters:
        print("You have already guessed this letter. ")
    elif guess not in answer_letters:
        print("Sorry, that letter is not in the word.")
        mistakes += 1

if mistakes == 0 and guess != answer_letters:
    print("You lost! ")


'''
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
