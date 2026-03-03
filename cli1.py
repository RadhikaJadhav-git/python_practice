# student_manager.py

students = []

def add_student(name, marks):
    students.append({"name": name, "marks": marks})

def display_students():
    for s in students:
        print(f"Name: {s['name']} | Marks: {s['marks']}")

add_student("Radhika", 85)
add_student("Amit", 90)
display_students()

