"""https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html"""

import random

medstr = ["a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
          "A", "B", "C", "D", "E", "F", "G", "H", "@", "$", "%", "&", "!", "?", "=", "+", "-", "*"]
weaka = ["spicy", "sweet", "sour", "dry", "bitter"]
weakb = ["orange", "strawberry", "peach", "cherry", "lemon", "chestnut"]


def passgenerator(strenght):
    yourpassword = []
    if strenght == 0:
        weakpass = weaka[random.randint(0, 4)]+weakb[random.randint(0, 4)]
        yourpassword.append(weakpass)
        yourpassword = "".join(yourpassword)
    else:
        numu = 0
        while numu < strenght*6:
            medstrpass = medstr[random.randint(0, 17*strenght)]
            yourpassword.append(medstrpass)
            numu += 1
        yourpassword = "".join(yourpassword)
    return yourpassword


while True:
    number = input("Would you like a 'weak', 'medium' or 'strong' password?\n>").lower()
    power = 0
    yesno = ""
    if number != "weak" and number != "medium" and number != "strong":
        print("Input 'weak', 'medium' or 'strong'.")
        continue
    else:
        if number == "medium":
            power = 1
        elif number == "strong":
            power = 2
    print("Your password is", passgenerator(power))
    while yesno == "":
        yesno = input("Would you like to get another password?\n>").lower()
        if yesno == "yes":
            pass
        elif yesno == "no":
            print("Goodbye!")
            quit()
        else:
            print("Say yes or no, please...")
            yesno = ""
