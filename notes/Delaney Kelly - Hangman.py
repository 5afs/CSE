import random
words = ["spinx", "dwarf", "bagpipes", "banjo", "pixel", "unzip", "zigzag", "oxygen", "mystify", "hyphen"]

answer_word = random.choices(words)
answer_letters = list(answer_word)

guess = input("Guess a Letter: ")


if guess == character(answer_letters):


for character in answer_letters:
    if character(guess) == character(answer_letters):  # replace with a *
        current_index = words.index(character)
        answer_letters.pop(current_index)
        answer_letters.insert(current_index, "*")
        print(answer_letters)




