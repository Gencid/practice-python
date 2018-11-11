"""https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html"""


def give_number():
    while True:
        try:
            num = int(input("Give me a number and I'll tell you if it's prime or not.\n>"))
            if num < 1:
                print("Actually, I want an integer higher than 0. Only positive numbers can be prime.")
                continue
            return num
        except ValueError:
            print("Input an integer, please.")


your_number = give_number()
divisors = [1, your_number]
for n in range(2, your_number):
    if your_number % n == 0:
        divisors.append(n), divisors.sort()
if divisors == [1, your_number]:
    print(your_number, "is a primer number!")
else:
    print("This is not a primer number.", divisors, "is a list of numbers that are divisors of {}.".format(your_number))
