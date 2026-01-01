students = {
    "Amit": 68,
    "Riya": 82,
    "Sneha": 74,
    "Rahul": 90
}

print("Students at Attendance Risk:\n")

for name, attendance in students.items():
    if attendance < 75:
        print(f"{name} → {attendance}% attendance")
