# Read file line by line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
