"""https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html"""

from Functions.FGuessingGameTwo import *


print("Quick, think of a number from 0 to 100!")
print("I'll try to guess it, and you must tell me if it's "
      "'\33[31mtoo low\33[0m' or '\33[31mtoo high\33[0m'")
print("Say '\33[34myes\33[0m' if the number is correct.")
input("Got it? Press Enter and I'll try to guess your number!")
if __name__ == "__main__":
    print("I did it! It took me", guess_number(), "tries.")
