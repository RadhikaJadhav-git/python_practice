# Reading data from a file
file = open("data.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)
