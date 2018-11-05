"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without
duplicates). Make sure your program works on two lists of different sizes.

Extras:

    1. Randomly generate two lists to test this
    2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to
       it soon)"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("List 1:", a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List 2:", b)
c = []
for item in a:
    if item in c:
        pass
    elif item in b:
        c.append(item)

print("Overlaped lists 1 and 2:", c)

d_size = random.randint(5, 15)
d_range = range(1, d_size+1)
d = []
for item in d_range:
    d.append(random.randint(0, 20)), d.sort()
print("List 3 (randomized):", d)
e_size = random.randint(5, 15)
e_range = range(1, e_size+1)
e = []
for item in e_range:
    e.append(random.randint(0, 20)), e.sort()
print("List 4 (randomized):", e)
f = []
for item in d:
    if item in f:
        pass
    elif item in e:
        f.append(item)
print("Overlaped lists 3 and 4:", f)

#  The 'Extra 2' is done in Exercise 10: List Overlap Comprehensions
