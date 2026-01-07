students = {
    "Ravi": [1, 1, 0, 1, 1],
    "Asha": [1, 0, 1, 1, 0],
    "Kiran": [1, 1, 1, 1, 1]
}

def attendance_percentage(record):
    return (sum(record) / len(record)) * 100

for name, record in students.items():
    print(name, "Attendance:", attendance_percentage(record), "%")
