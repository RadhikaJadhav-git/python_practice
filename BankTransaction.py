balance = 10000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

deposit(2000)
withdraw(5000)
withdraw(10000)
print("Final Balance:", balance)
