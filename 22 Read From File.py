"""https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html"""
import re

dictnames = dict()
textnames = open("nameslist.txt", "r")
for linenames in textnames:
    names = linenames.split()
    for name in names:
        if name not in dictnames:
            dictnames[name] = 1
        else:
            dictnames[name] += 1
for itemnames in dictnames:
    print(itemnames, "is repeated", dictnames[itemnames], "times.")

dictsun = dict()
sunnyplace = ""
sunnynumber = 0
textsun = open("Training_01.txt", "r")
for linesun in textsun:
    if re.search("sun_", linesun):
        sunnynumber = linesun.find("sun_")
        sunnyplace = (linesun[:sunnynumber])
        if sunnyplace not in dictsun:
            dictsun[sunnyplace] = 1
        else:
            dictsun[sunnyplace] += 1
for itemsun in dictsun:
    print(itemsun, "is repeated", dictsun[itemsun], "times.")
