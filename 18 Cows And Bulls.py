"""https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html"""

from Functions.FCowsAndBulls import *

print("This is a Cows and Bulls game. The computer will generate a four digit number and you'll have to\n"
      "guess it. The game will tell you how many Cows and Bulls you have: Cows are correct numbers in the\n"
      "correct place. Bulls are correct numbers in incorrect places.\n"
      "To exit the game, type 'exit'. Good Luck!")

if __name__ == "__main__":
    cowbull_game()
