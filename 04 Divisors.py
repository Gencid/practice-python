"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is
a divisor of 26 because 26 / 13 has no remainder.)"""

while True:
    try:
        num = abs(int(input("Give me a number!\n>")))
        break
    except ValueError:
        print("Input an integer, please.")
one_to_num = range(1, num+1)
divisors = []
for n in one_to_num:
    if num % n == 0:
        divisors.append(n)
print(divisors, "is a list of numbers that are divisors of {}.".format(num))
