print("1. KM to Miles")
print("2. Miles to KM")

choice = int(input("Choose: "))

if choice == 1:
    km = float(input("Enter KM: "))
    print("Miles:", round(km * 0.621371, 3))

else:
    miles = float(input("Enter Miles: "))
    print("KM:", round(miles / 0.621371, 3))
