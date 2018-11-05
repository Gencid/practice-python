"""Take a list, say for example this one:

     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this
       list in it and print out this new list.
    2. Write this in one line of Python.
    3. Ask the user for a number and return a list that contains only elements from the original list a that are
       smaller than that number given by the user."""

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
