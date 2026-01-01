expenses = {
    "Rent": 8000,
    "Food": 3500,
    "Travel": 2200,
    "Internet": 900
}

highest = max(expenses, key=expenses.get)

print("Expense Summary")
print("---------------")
print("Highest Spending Category:", highest)
print("Amount:", expenses[highest])
