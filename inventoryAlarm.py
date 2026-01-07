inventory = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 15,
    "Monitor": 2
}

threshold = 5

for item, qty in inventory.items():
    if qty < threshold:
        print(f"Low stock alert: {item} ({qty} left)")
