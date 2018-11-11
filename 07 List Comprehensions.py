"""https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [item for item in a if item % 2 == 0]
print(b)
