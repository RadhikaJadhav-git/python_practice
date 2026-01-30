with open("data.txt", "r") as f:
    words = f.read().split()
    print("Word count:", len(words))
