def guess_letter(letters, blanks, chosen, word):
    the_chosen = chosen
    the_word = word
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
    for letter in the_word:
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
    if all_filled is True:
        print("Congratulations! You guessed the word! Yay!")
    return all_filled


def drawing(hangman):
    lives_left = hangman
    if lives_left == 5:
        print(" O")
    elif lives_left == 4:
        print(" O\n |")
    elif lives_left == 3:
        print(" O\n/|")
    elif lives_left == 2:
        print(" O\n/|\\")
    elif lives_left == 1:
        print(" O\n/|\\\n/")
    elif lives_left == 0:
        print(" O\n/|\\\n/ \\")
