"""https://www.practicepython.org/exercise/2014/01/29/01-character-input.html"""

import datetime

datetoday = datetime.datetime.now()
yeartoday = datetoday.year
name = input("Give me your name:\n>")
age = -1
repeats = 0
while age < 0:
    try:
        age = int(input("How old are you?\n>"))
    except ValueError:
        print("Input an whole number, please")
        age = -1
        continue
    if age < 0:
        print("You can't be less than 0 years old! Unless you don't exist yet, that is...\n"
              "If you exist in the present and you are not a time traveler, please try again. Else, just try to not"
              "break the universe... or something.")
        continue
hundredyears = str(yeartoday+(100-age))
while repeats <= 0:
    try:
        repeats = int(input("Now give me a number greater than 0\n>"))
    except ValueError:
        print("Input an whole number, please")
        repeats = 0
        continue
    if repeats <= 0:
        print("That number is not greater than 0.")
        continue
if age >= 100:
    print(("Hello, " + name + ". You are really old!\n") * repeats)
else:
    print(("Hello, " + name + ". You will turn 100 in the year " + hundredyears + ".\n") * repeats)
