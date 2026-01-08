students = {}

def add_student(roll, name, marks):
    students[roll] = {"name": name, "marks": marks}

def display_students():
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

add_student(1, "Rahul", 85)
add_student(2, "Anita", 90)
display_students()
