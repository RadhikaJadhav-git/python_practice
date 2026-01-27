class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 5 * 4

class Circle(Shape):
    def area(self):
        return 3.14 * 3 * 3

shapes = [Rectangle(), Circle()]
for s in shapes:
    print(s.area())
