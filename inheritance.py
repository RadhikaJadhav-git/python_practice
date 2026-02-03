class Person:
    def show(self):
        print("This is a Person class")

class Employee(Person):
    def display(self):
        print("This is an Employee class")

emp = Employee()
emp.show()
emp.display()
