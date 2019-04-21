"""https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html"""


def guess_letter(letters, blanks, chosen):
    the_chosen = chosen
    while True:
        your_letter = input("Choose a letter:\n>").upper()
        if len(your_letter) != 1:
            print("Input one letter, please.")
            continue
        if ord(your_letter) < ord("A") or ord(your_letter) > ord("Z"):
            print("You need to input a letter from A to Z.")
            continue
        if your_letter in the_chosen:
            print("You already chose that letter.")
            continue
        break
    num_letter = 0
    for letter in chosen_word:
        if letters[num_letter] == your_letter:
            blanks[num_letter] = letter + " "
        num_letter += 1
    print("".join(blanks))
    return your_letter


def filled_blanks(blanks):
    all_filled = True
    for letter in blanks:
        if letter == "_ ":
            all_filled = False
    return all_filled


chosen_word = "EVAPORATE"
letters_list = []
blanks_list = []
chosen_letters = []
for character in chosen_word:
    blanks_list.append("_ ")
    letters_list.append(character)
print("".join(blanks_list))

while filled_blanks(blanks_list) is False:
    chosen_letters.append(guess_letter(letters_list, blanks_list, chosen_letters))
