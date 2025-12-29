level = int(input("Enter water level (0–100): "))

if level <= 20:
    print("Motor ON – Tank Low")
elif level >= 90:
    print("Motor OFF – Tank Full")
else:
    print("Water level normal")
