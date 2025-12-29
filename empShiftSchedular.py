employees = ["Amit", "Neha", "Ravi", "Pooja"]
shifts = ["Morning", "Evening", "Night"]

for i in range(len(employees)):
    print(employees[i], "→", shifts[i % 3])
