"""https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html"""

while True:
    try:
        num = int(input("Give me a number.\n>"))
        break
    except ValueError:
        print("Input an integer, please.")
if num % 4 == 0:
    print(num, "is a multiple of 4!")
elif num % 2 == 0:
    print(num, "is an even number!")
else:
    print(num, "is an odd number!")
while True:
    try:
        check = int(input("Now give me another number.\n>"))
        break
    except ValueError:
        print("Input an integer, please")
if num % check == 0:
    print(num, "is a multiple of", check)
else:
    print("Your first number does not divide evenly into your second number...")
