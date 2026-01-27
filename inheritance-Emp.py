class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")

class Manager(Employee):
    def manage(self):
        print(self.name, "is managing")

m = Manager("Radhika")
m.work()
m.manage()
