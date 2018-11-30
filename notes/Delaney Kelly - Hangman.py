import random
words = ["spinx", "dwarf", "bagpipes", "banjo", "pixel", "unzip", "zigzag", "oxygen", "mystify", "hyphen"]

answer_word = random.choice(words)
answer_letters = list(answer_word)
blank_answer = []

for item in answer_letters:
        # Make *s for letters in a new list
        current_index = answer_letters.index(item)
        blank_answer.insert(current_index, "*")


print("The word is %d letters long" % len(answer_letters))
guess = input("Guess a letter: ")




'''
if guess == answer_letters:

for character in answer_letters:
    if character(guess) == character(answer_letters):  # replace with a *
        current_index = words.index(character)
        answer_letters.pop(current_index)
        answer_letters.insert(current_index, "*")
        print(answer_letters)
'''





