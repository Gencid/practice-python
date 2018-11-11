"""https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Our list is {}.".format(a))
b = []
for i in a:
    b.append(i) if i < 5 else b
print(b, "are lower than 5")
while True:
    try:
        your_num = int(input("Now give me a number.\n>"))
        break
    except ValueError:
        print("Input an integer, please")
c = []
for i in a:
    c.append(i) if i < your_num else c
print(c, "are lower than {}.".format(your_num))
