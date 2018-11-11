"""https://www.practicepython.org/exercise/2014/02/26/04-divisors.html"""

while True:
    try:
        num = abs(int(input("Give me a number!\n>")))
        break
    except ValueError:
        print("Input an integer, please.")
divisors = []
for n in range(1, num+1):
    if num % n == 0:
        divisors.append(n)
print(divisors, "is a list of numbers that are divisors of {}.".format(num))
