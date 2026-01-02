days_late = int(input("Enter number of late days: "))

if days_late <= 0:
    fine = 0
elif days_late <= 5:
    fine = days_late * 2
else:
    fine = days_late * 5

print("Total Fine: ₹", fine)
