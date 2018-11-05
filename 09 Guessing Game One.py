"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell
them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons
from the very first exercise)

Extras:

    · Keep the game going until the user types “exit”
    · Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

x = random.randint(1, 9)
print("I selected a number from 1 to 9. Can you guess it?")
guesses = 0

while True:
    inp_y = input("Choose a number.\n>")
    if inp_y == "exit":
        print("Oh, okay. For your information, the number was {}. Bye~".format(x))
        quit()
    try:
        y = int(inp_y)
        if y < 1 or y > 9:
            print("Type a whole number from 1 to 9")
            continue
    except ValueError:
        print("Type a whole number from 1 to 9")
        continue
    guesses += 1
    if y == x:
        print("Very good!")
        if guesses == 1:
            print("You did it in only 1 guess! Are you a psychic?")
            quit()
        else:
            print("It took you {} guesses.".format(guesses))
            quit()
    else:
        print("Ha! Wrong answer! Try again.")
        continue
