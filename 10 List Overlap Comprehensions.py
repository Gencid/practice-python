"""This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in
a different way.

Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without
duplicates). Make sure your program works on two lists of different sizes. Write this using
at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers
pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can
either choose to use the original directive and read about the set command in Python 3.3, or try to implement this
on your own and use at least one list comprehension in the solution.

Extra:

    · Randomly generate two lists to test this"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("List 1:", a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List 2:", b)
c = list(set([item for item in a if item in b]))

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
f = list(set([item for item in d if item in e]))
print("Overlaped lists 3 and 4:", f)
