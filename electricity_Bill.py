units = int(input("Enter units consumed: "))

bill = 0
if units <= 100:
    bill = units * 3
elif units <= 300:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 200 * 5 + (units - 300) * 7

print("Electricity Bill:", bill)
