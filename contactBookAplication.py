contacts = {}

while True:
    print("\n1.Add 2.View 3.Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        print(contacts)
    else:
        break
