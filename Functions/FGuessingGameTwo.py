import random


def guess_number():
    lowest = 0
    highest = 100
    tries = 0
    # First, it will guess randomly until getting a highest and a lowest
    while lowest == 0 or highest == 100:
        if lowest > highest:
            print("Don't cheat!")
            quit()
        looper1 = True
        randomguess = random.randint(lowest, highest)
        print("My guess is", randomguess)
        while looper1 is True:
            answer = input(">").lower()
            if answer == "too low":
                lowest = randomguess+1
                tries += 1
                looper1 = False
            elif answer == "too high":
                highest = randomguess-1
                tries += 1
                looper1 = False
            elif answer == "yes":
                tries += 1
                return tries
            else:
                print("Please, tell me if it's '\33[31mtoo low\33[0m' or '\33[31mtoo high\33[0m'"
                      ", or say '\33[34myes\33[0m' if the number is correct.")
    # Once it has a highest and a lowest, it will guess by trying the number in the middle
    while True:
        halfguess = int(lowest+(highest-lowest)/2)
        print("My guess is", halfguess)
        looper2 = True
        while looper2 is True:
            answer = input(">").lower()
            if answer == "too low":
                lowest = halfguess + 1
                tries += 1
                looper2 = False
            elif answer == "too high":
                highest = halfguess - 1
                tries += 1
                looper2 = False
            elif answer == "yes":
                tries += 1
                return tries
            else:
                print("Please, tell me if it's '\33[31mtoo low\33[0m' or '\33[31mtoo high\33[0m'"
                      ", or say '\33[34myes\33[0m' if the number is correct.")
