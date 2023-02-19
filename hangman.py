import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter:").lower()
word_length = len(chosen_word)

print(f"The solution is {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)
