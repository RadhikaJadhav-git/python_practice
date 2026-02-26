s = "hello world"

count = {}

for char in s:
    if char != " ":
        count[char] = count.get(char, 0) + 1

print(count)