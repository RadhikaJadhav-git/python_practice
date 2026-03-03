class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_college(cls):
        print(cls.college)

    @staticmethod
    def add(a, b):
        return a + b

Student.show_college()
print(Student.add(10, 20))
