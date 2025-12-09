def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice = int(input("Choose: "))

if choice == 1: print("Result:", add(a,b))
elif choice == 2: print("Result:", sub(a,b))
elif choice == 3: print("Result:", mul(a,b))
else: print("Result:", div(a,b))
