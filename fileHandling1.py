# Write and read from a file

# Writing
with open("sample.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("File handling example")

# Reading
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
