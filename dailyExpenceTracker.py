expenses = {
    "Food": 250,
    "Travel": 120,
    "Books": 400,
    "Coffee": 90
}

total = sum(expenses.values())
highest = max(expenses, key=expenses.get)

print("Total Expense:", total)
print("Highest Expense Category:", highest)
