# calculator.py

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))
print(calculator(10, 5, "mul"))
