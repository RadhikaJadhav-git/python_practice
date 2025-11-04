print("Enter marks for 5 subjects (out of 100):")
marks = []
for i in range(1, 6):
    m =float(input(f"Subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >=60:
    grade = 'C'
elif percentage >=50:
    grade = 'D'
else:
    grade = 'F'
    
    
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
