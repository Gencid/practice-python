"""https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("List 1:", a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List 2:", b)
c = list(set([item for item in a if item in b]))

print("Overlaped lists 1 and 2:", c)

d_size = random.randint(5, 15)
d = random.sample(range(20), d_size)
d.sort()
print("List 3 (randomized):", d)
e_size = random.randint(5, 15)
e = random.sample(range(20), e_size)
e.sort()
print("List 4 (randomized):", e)
f = list(set([item for item in d if item in e]))
print("Overlaped lists 3 and 4:", f)
