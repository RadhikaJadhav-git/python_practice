from datetime import date

exp_year = int(input("Enter expiry year: "))
exp_month = int(input("Enter expiry month: "))

today = date.today()

if exp_year < today.year or (exp_year == today.year and exp_month < today.month):
    print("Medicine Expired ❌")
else:
    print("Medicine Safe to Use ✅")
