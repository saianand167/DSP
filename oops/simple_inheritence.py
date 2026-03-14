class human:
    def __init__(self):
        self.eyes=2
        self.nose=1
    def eat(self):
        print("ya bro i can eat")
    def work(self):
        print("ya bro i can work")
class male(human):
    def __init__(self,legs):
        super().__init__() #when we use this constructor we need to use super
        self.legs=legs
    def work(self):
        super().work()
        print("i can do work")
    def crazy(self):
        print("i am crazy")
male1=male(2)
male1.work()
# male1.eat()
print(male1.legs)
print(male1.eyes)
