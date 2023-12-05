class Rectangle:
    def __init__(self, length, breadth):
        self.k = length
        self.b = breadth

    def rec(self, ):
        area = self.k * self.b
        return area


rectangle_1 = Rectangle(5, 9)
print(rectangle_1.rec())
