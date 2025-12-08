filename = "notes.txt"

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        note = input("Write your note: ")
        with open(filename, "a") as file:
            file.write(note + "\n")
        print("Note added!")

    elif choice == 2:
        print("\n--- Your Notes ---")
        with open(filename, "r") as file:
            print(file.read())

    else:
        print("Goodbye!")
        break
