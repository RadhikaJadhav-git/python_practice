dictionary = {
    "approach": "a way of dealing with something.",
    "compute": "calculate or process data",
    "variable": "a container for storing values."
}

word = input("Enter a word: ").lower()

if word in dictionary:
    print(word, ":", dictionary[word])
else:
    print("Word not found!")
