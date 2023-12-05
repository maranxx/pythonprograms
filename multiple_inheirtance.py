class Human:
    def __init__(self, heart):
        self.eye = 1
        self.nose = 1
        self.heart=1
    def eat(self):
        print('i can eat')
    def work(self):
        print("ican work")


class Male:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("i can walk")
    def work(self):
        print("i can fight")


class Boy(Human, Male):
    def __init__(self, name, heart , language):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.language = language
    def work(self):
        print("i go to school")
    def display(self):
        print(F"hi i am {self.name}, i work in {self.language} language")


boy_1 = Boy("rick",1, "python")
print(boy_1.name)
print(boy_1.heart,boy_1.language)
boy_1.display()
#boy_1.eat()
#boy_1.work()
#Male.work(boy_1)
#boy_1.work()
#print(Boy.mro())

