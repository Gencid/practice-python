"""https://www.practicepython.org/exercise/2014/11/11/20-element-search.html"""


def binary_search(lista, number):
    while True:
        middle = len(lista)//2
        if number >= lista[middle]:
            if number == lista[middle]:
                print("Nice, that number is in the list!")
                return True
            lista = lista[middle:]
        else:
            lista = lista[:middle]
        if middle == 0:
            print("That number is not in the list!")
            return False


def givenumber():
    while True:
        try:
            inputnum = (int(input(">")))
            return inputnum
        except ValueError:
            print("That's not a number...")
            continue


lostlist = [4, 8, 15, 16, 23, 42]
print("Give me a number to check if it's in our list.\n"
      "By the way, none of them is higher than 50")
while True:
    if binary_search(lostlist, givenumber()) is True:
        print("Well done!")
        quit()
    else:
        print("Try again.")
        continue
