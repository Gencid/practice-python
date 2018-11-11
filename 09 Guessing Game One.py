"""https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html"""

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
