books = {
    "Python": 4,
    "Django": 12,
    "Data Analysis": 3,
    "Java": 9
}

print("Low Stock Books:\n")

for book, qty in books.items():
    if qty < 5:
        print(f"{book} → Only {qty} copies left")
