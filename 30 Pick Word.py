"""https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html"""

import random

a = []

with open("sowpods.txt", "r") as pod:
    line = pod.readline().strip()
    while line:
        line = pod.readline()
        a.append(line)
b = random.choice(a)
print(b)
