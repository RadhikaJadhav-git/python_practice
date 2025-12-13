marks = []

for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))

average = sum(marks) / len(marks)

print("Average Marks:", average)

if average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
