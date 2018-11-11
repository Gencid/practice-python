"""https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html"""


def remodupsset(listzero):
    listzero = set(listzero)
    listzero = list(listzero)
    return listzero


def remodupsloop(listzero):
    listloop = []
    for item in listzero:
        if item not in listloop:
            listloop.append(item)
    return listloop


listone = remodupsset(["Horse", "Rooster", "Rabbit", "Ox", "Dragon", "Rooster", "Dog"])
listtwo = remodupsset(["Wood", "Metal", "Fire", "Fire", "Water", "Wind", "Metal"])
print(listone, listtwo)

listone = remodupsloop(["Horse", "Rooster", "Rabbit", "Ox", "Dragon", "Rooster", "Dog"])
listtwo = remodupsloop(["Wood", "Metal", "Fire", "Fire", "Water", "Wind", "Metal"])
print(listone, listtwo)
