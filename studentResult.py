marks = {
    "Math": 85,
    "Science": 72,
    "English": 90,
    "History": 65
}

total = sum(marks.values())
percentage = total / len(marks)

if percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
elif percentage >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)