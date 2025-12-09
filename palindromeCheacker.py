word = input("Enter word: ").lower()

if word == word[::-1]:
    print("It is a palindrome!")
else:
    print("Not a palindrome.")
