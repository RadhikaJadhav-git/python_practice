word = "Python"
with open("data.txt", "r") as f:
    print(word, "found" if word in f.read() else "not found")
