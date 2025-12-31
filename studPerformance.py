marks = [78, 85, 69, 90, 88]
average = sum(marks) / len(marks)

if average >= 85:
    grade = "A"
elif average >= 70:
    grade = "B"
else:
    grade = "C"

print("Average Marks:", average)
print("Grade:", grade)
