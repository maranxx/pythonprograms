class Human:
    def __init__(self, num_heart):
        self.eyes = 2
        self.heart = num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male(Human):
    def __init__(self, name):
        self.name = name

    def fight(self):
        print("i can fight")


class Boy(Male):
    def __init__(self,  num_heart, name, can_dance):
        Human.__init__(self, num_heart)
        Male.__init__(self, name)
        self.dance = can_dance
    def work(self):
        super().work()
        print("i can play")


boy_1 = Boy(1, "rick", True)
boy_1.fight()
boy_1.work()
Human.work(boy_1)
print(boy_1.eyes)
