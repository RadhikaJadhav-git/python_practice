numbers = [10, 5, 20, 8, 15]

numbers = list(set(numbers))   # remove duplicates
numbers.sort()

print("Second largest:", numbers[-2])
