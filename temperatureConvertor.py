def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Choose: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", round(c_to_f(c), 2))
else:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", round(f_to_c(f), 2))
