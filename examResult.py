marks = int(input("Enter marks: "))

if marks >= 75:
    result = "Distinction"
elif marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Result:", result)
