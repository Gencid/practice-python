"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
that reads the same forwards and backwards.)"""

your_word = input("Type a palindrome:\n>")
reverse_word = your_word[::-1]
if your_word == reverse_word:
    print("It's a palindrome!")
else:
    print("This is not a palindrome...")
