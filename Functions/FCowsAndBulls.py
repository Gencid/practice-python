import random


def cowbull_generator():
    intstr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cowbull = []
    for num in range(0, 4):
        cowbull.append(intstr[random.randint(0, 9)])
    return cowbull


def guess_number():
    while True:
        your_guess = input("Input a number from 0000 to 9999\n>")
        try:
            int(your_guess)
        except ValueError:
            print("That's not a number!")
            continue
        if len(your_guess) != 4:
            print("Four digits, please.")
            continue
        return your_guess


def cowbull_game():
    cowbull = cowbull_generator()
    # print(cowbull) # Prints the generated number for testing purposes
    count_tries = 0
    cows_bulls = [0, 0]
    while cows_bulls == [0, 0]:
        guessed = guess_number()
        cows_bulls = [0, 0]
        count_0to4 = 0
        count_tries += 1
        for letter in guessed:
            if letter in cowbull:
                if letter == cowbull[count_0to4]:
                    cows_bulls[0] += 1
                else:
                    cows_bulls[1] += 1
            count_0to4 += 1
        if cows_bulls == [4, 0]:
            print("You have", cows_bulls[0], "cows and", cows_bulls[1], "bulls. You did it!")
            print("You needed", count_tries, "tries.")
            quit()
        else:
            print("You have", cows_bulls[0], "cows and", cows_bulls[1], "bulls.")
            cows_bulls = [0, 0]
            continue
