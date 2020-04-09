import random

words = ["salam", "eggplant", "python", "turtle", "milkyway", "computer", "galaxy", "desk", "podcast", "resolution", "yahoo",
         "program", "dictionary", "revolution", "son", "daughter", "software", "sweethome",
         "firetruck", "car", "food", "coronavirus", "contagious", "coding", "water", "radio",
         "break", "yunus", "plant", "flower", "sunshine", "cleaning"]

secret_word = random.choice(words)

dashes = ""
for i in range(len(secret_word)):
    dashes += "-"


def get_guess():
    g = input("Guess: ")
    while True:
        if len(g) > 1:
            print("Your guess must have exactly one character!")
            g = input("Guess: ")
        elif g.isupper() or g.isdigit():
            print("Your guess must be a lowercase letter!")
            g = input("Guess: ")
        else:
            return g


def update_dashes(secretWord, current_state, recentGuess):
    res = ""

    for i in range(len(secretWord)):
        if secretWord[i] == recentGuess:
            res += recentGuess
        else:
            res += current_state[i]
    return res


guesses_left = 10
guessList = []


while True:
    print(str(guesses_left) + " incorrect guesses left.")
    print(dashes)
    if dashes == secret_word:
        print(f"Congrats! You win. The word was:  {secret_word}")
        break
    g = get_guess()
    while g in guessList:
        print("You already guessed the letter, guess again!")
        g = get_guess()
    guessList.append(g)
    if g in secret_word:
        dashes = update_dashes(secret_word, dashes, g)
    else:
        guesses_left -= 1
        if guesses_left == 0:
            print("You lose. The word was: " + secret_word)
            break
