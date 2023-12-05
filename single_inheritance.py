class Human:
    def __init__(self, num_heart):
        self.eyes = 2
        self.nose = 1
        self.heart = num_heart

    def work(self):
        print("i can work")

    def eat(self):
        print("i can eat")


class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)  # after defining attributes or data to subclass we cant access attributes in super class, thus so to access we need use
                                     # super().__init__() function
        self.name = name
    def gym(self):
        print("i go gym")

    def work(self):
        super().work()  # if overriding takes place and we need to access super class as well as sub class use super() function
        print("i can sing")


male_1 = Male("rick",1)
male_1.gym()
male_1.work()
male_1.eat()
print(male_1.nose)
print(male_1.eyes,male_1.name)
print(male_1.heart
      )
