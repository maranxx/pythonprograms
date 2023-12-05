class Circle:
    pi = 3.14  # class  object attribute

    def __init__(self, radius):
        self.radius = radius
        self.area= Circle.pi*radius*radius

    def get_circum(self):
        return 2 * Circle.pi * self.radius  # to use a class object attribute always use class name before it


circle_1 = Circle(4)
print(circle_1.get_circum())
circle_2 = Circle(5)
print(circle_2.get_circum())
print(circle_1.area)
print(circle_2.area)

