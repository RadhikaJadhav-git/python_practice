with open("file1.txt", "r") as source:
    content = source.read()

with open("file2.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.")
