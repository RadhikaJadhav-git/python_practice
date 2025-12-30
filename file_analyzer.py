import os

path = input("Enter file path: ")

if os.path.exists(path):
    size = os.path.getsize(path)
    print("File size:", size, "bytes")
else:
    print("File not found")
