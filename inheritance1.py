class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("Salary:", self.salary)


e1 = Employee("Radhika", 50000)
e1.show()
e1.display()
