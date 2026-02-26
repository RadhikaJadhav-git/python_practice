balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance and amount % 100 == 0:
    balance -= amount
    print("Please collect cash")
else:
    print("Invalid or insufficient balance")

print("Remaining balance:", balance)
