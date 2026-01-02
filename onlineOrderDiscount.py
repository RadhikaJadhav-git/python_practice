amount = float(input("Enter order amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

print("Discount Applied: ₹", discount)
print("Final Amount: ₹", amount - discount)
