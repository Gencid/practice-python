"""https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html"""


def overlapper(lista, listb):
    list_overlap = []
    for item in listb:
        if item in lista:
            list_overlap.append(item)
    list_overlap.sort()
    return list_overlap


prime_numbers = []
happy_numbers = []
textprime = open("primenumbers.txt")
for lineprime in textprime:
    primes = lineprime.split()
    for prime in primes:
        prime = int(prime)
        prime_numbers.append(prime)
texthappy = open("happynumbers.txt")
for linehappy in texthappy:
    happies = linehappy.split()
    for happy in happies:
        happy = int(happy)
        happy_numbers.append(happy)

print(overlapper(prime_numbers, happy_numbers))
