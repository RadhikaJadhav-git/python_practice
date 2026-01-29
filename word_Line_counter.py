with open("sample.txt", "r") as file:
    text = file.read()

lines = text.split("\n")
words = text.split()

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", len(text))
