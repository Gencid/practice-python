"""https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html"""


def listends(listdef):
    return [listdef[0], listdef[-1]]


lista = listends([2, 4, 6, 8])
print(lista)
listb = listends([3, 6, 9, 12, 15, 18, 21])
print(listb)
listc = listends([5, 10, 15, 20, 25])
print(listc)
