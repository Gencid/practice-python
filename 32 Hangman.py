"""https://www.practicepython.org/exercise/2017/01/10/32-hangman.html"""

import random
from Functions.FHangman import *

while True:
    words_list = []
    with open("sowpods.txt", "r") as pod:
        line = pod.readline()
        while line:
            line = pod.readline()
            words_list.append(line)
    random_word = str(random.choice(words_list)).strip()
    letters_list = []
    letters_in_word = {None}
    blanks_list = []
    chosen_letters = {None}
    lives = 6
    for character in random_word:
        blanks_list.append("_ ")
        letters_list.append(character)
        letters_in_word.add(character)
    print("".join(blanks_list))
    if __name__ == "__main__":
        lol = filled_blanks
        while filled_blanks(blanks_list) is False:
            adding = (guess_letter(letters_list, blanks_list, chosen_letters, random_word))
            chosen_letters.add(adding)
            if adding not in letters_in_word:
                lives -= 1
            drawing(lives)
            if lives == 0:
                print("You lost the game!")
                print("The word was " + random_word + ".")
                break
    yesno = ""
    while yesno == "":
        yesno = input("Do you want to play again?\n>").lower()
        if yesno == "yes" or yesno == "y":
            print("Great, let's play again!")
        elif yesno == "no" or yesno == "n":
            print("Okay. Let's play again any other time. Bye!")
            quit()
        else:
            print("Input yes/y or no/n, please.")
            yesno = ""
            continue
