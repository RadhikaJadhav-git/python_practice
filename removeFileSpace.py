with open("data.txt", "r") as f:
    lines = [line for line in f if line.strip()]

with open("clean.txt", "w") as f:
    f.writelines(lines)
