with open("data.txt", "r") as f:
    print("Lines:", sum(1 for _ in f))
