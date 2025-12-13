word = input("Enter word to search: ")

with open("data.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word found in file.")
else:
    print("Word not found.")
