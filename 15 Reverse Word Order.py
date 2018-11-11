"""https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html"""


def sdrawkcab(words):
    wordsplit = words.split()
    wordreverse = wordsplit[::-1]
    phrasereverse = " ".join(wordreverse)
    return phrasereverse


yourphrase = sdrawkcab(input("Say a phrase!\n"))
print(yourphrase)
