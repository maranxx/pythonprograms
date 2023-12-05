class A:
    def display(self):
        print("a from A class")
class B(A):
    def show(self):
        print("b from B class")
class C:
    def fun(self):
        print("c from c class")
class D(B,C):
    def display(self):
     super().display()
    print("display fromD class")

d1=D()
d1.display()
A.display(d1)
