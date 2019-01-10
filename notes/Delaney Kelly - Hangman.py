import random
words = ["shouldn't", "dwarf", "elephant", "banjo", "pixel", "unzip", "don't", "green", "mystery", "bagpipes", "water"]

answer_word = random.choice(words)

answer_letters = list(answer_word)
blank_answer = []
mistakes = 8

for item in answer_letters:
    # Make _s for letters in a new list
    current_index = answer_letters.index(item)
    blank_answer.insert(current_index, "_ ")

print("The answer is %d letters long" % len(answer_letters))
print("".join(blank_answer))  # print a joined list

while mistakes > 0:
    guess = input("Guess a letter: ")  # should go in the loop
    # if guess == character in answer_letters:


'''
you get 8 guesses
if guess == answer_letters:

for character in answer_letters:
    if character(guess) == character(answer_letters):  # replace with a *
        current_index = words.index(character)
        answer_letters.pop(current_index)
        answer_letters.insert(current_index, "*")
        print(answer_letters)
'''





