class Human:
    def __init__(self, name, age):
        print("calling it rom init")
        self.name = name
        self.age = age
    def eat(self):
        print("i can eat")

class Male(Human):
    def __init__(self,real,sports):
        self.real=real
        self.sports=sports
    def work(self):
        print("i can work")

class Female(Human):
    def __init__(self, name, age, working):
        Human.__init__(self, name, age)
        self.working = working
    def fight(self):
        print("i can fight")

#female_1=Female("izumi", 18,True)
#print(female_1.name)
male_1=Male("naruto",12)


