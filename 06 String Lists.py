"""https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html"""

your_word = input("Type a palindrome:\n>")
reverse_word = your_word[::-1]
if your_word == reverse_word:
    print("It's a palindrome!")
else:
    print("This is not a palindrome...")
