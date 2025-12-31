books = {
    "Python": 15,
    "Java": 8,
    "Data Science": 20,
    "Django": 12
}

print("High Demand Books:\n")

for book, issued in books.items():
    if issued >= 10:
        print(f"{book} → {issued} times issued")
