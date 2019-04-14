"""https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html"""


def maxvar(vara, varb, varc):
    if vara > varb:
        if vara > varc:
            return vara
        elif varc > vara:
            return varc
        elif varc == vara:
            print("Two of your variables are equal. They are:")
            return varc
    elif varb > vara:
        if varb > varc:
            return varb
        elif varc > varb:
            return varc
        elif varc == varb:
            print("Two of your variables are equal. They are:")
            return varc
    elif vara == varb:
        if varc > vara and varc > varb:
            return varc
        elif varc < vara and varc < varb:
            print("Two of your variables are equal. They are:")
            return varb
        else:
            print("All of your variables are equal! They are:")
            return vara


while True:
    try:
        onev = int(input("Give me a number.\n>"))
        break
    except ValueError:
        print("I need a number, please")
        continue

while True:
    try:
        twov = int(input("Now give me another number.\n>"))
        break
    except ValueError:
        print("I need a number, please")
        continue

while True:
    try:
        threev = int(input("Give me one last number.\n>"))
        break
    except ValueError:
        print("I need a number, please")
        continue

print("The biggest variable is:")
print(maxvar(onev, twov, threev))
