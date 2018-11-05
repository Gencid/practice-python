"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to
the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    1. If the number is a multiple of 4, print out a different message.
    2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
       If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

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
