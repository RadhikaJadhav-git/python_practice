names = ["Radhika", "Amit", "Sneha"]
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
