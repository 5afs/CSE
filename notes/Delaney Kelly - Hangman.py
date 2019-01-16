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
    guessed_letters.append(guess)
    if blank_answer == answer_letters:  # won
        mistakes = 0
        print("Yay!, you won")
        continue

    guess = input("Guess a letter: ")  # should go in the loop

    if guess in answer_letters and guess not in guessed_letters:
        guessed_letters.append(guess)

        for i in range(len(answer_letters)):  # A for loop that goes through each index
            if answer_letters[i] == guess:
                blank_answer[i] = guess
        print("".join(blank_answer))

    elif guess in guessed_letters:  # already guessed
        print("You have already guessed this letter.")

    elif guess not in answer_letters and guess not in guessed_letters:  # haven't guessed before, not correct
        guessed_letters.append(guess)
        mistakes -= 1
        print("That letter is not in the word.")

if mistakes == 0 and blank_answer != answer_letters:
    print("You lost! The answer was: %s" % answer_word)
