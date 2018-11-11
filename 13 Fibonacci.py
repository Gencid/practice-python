"""https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html"""


def fibonacci(rango):
    num1 = 0
    num2 = 1
    listacci = [1]
    for numitem in range(1, rango):
        listacci.append(num1 + num2)
        num3 = num1
        num1 = num2
        num2 = num3 + num1
    return listacci


while True:
    try:
        fibint = int(input("How many Fibonacci numbers would you like to generate?\n>"))
        if fibint <= 0:
            print("Input an integer greater than 0, please")
        else:
            break
    except ValueError:
        print("Input an integer greater than 0, please.")

fibprint = fibonacci(fibint)
print(fibprint)
