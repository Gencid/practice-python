"""https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html"""

import random


def overlapper(listone, listtwo):
    listthree = list(set(listone + listtwo))
    listthree.sort()
    return listthree


print(overlapper([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

ronesize = range(1, random.randint(5, 15)+1)
rone = []
for item in ronesize:
    rone.append(random.randint(0, 20)), rone.sort()
print("Random List 1:", rone)
rtwosize = range(1, random.randint(5, 15)+1)
rtwo = []
for item in rtwosize:
    rtwo.append(random.randint(0, 20)), rtwo.sort()
print("Random List 2:", rtwo)
roverlap = (overlapper(rone, rtwo))
print("Overlaped random lists:", roverlap)
