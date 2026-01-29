def add_note():
    with open("notes.txt", "a") as file:
        note = input("Enter your note: ")
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    with open("notes.txt", "r") as file:
        print(file.read())

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_note()
    elif ch == "2":
        view_notes()
    elif ch == "3":
        break
