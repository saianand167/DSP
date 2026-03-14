# class std:
#     def __init__(self,name,age=10):
#         self.name=name
#         self.age=age
#     def __init__(self,mobile):
#         self.mobile=mobile
#     def set_age(self,age):
#         if age<20:
#             print("invalid age")

# std1=std("raj",15)
# std1=std("9876543210")
# std1.set_age(std1.age)
# print(std1.name,std1.age,std1.mobile)
# # only last constructor will be considered

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
c1=circle(5)
print("Area:",c1.area())
print("Circumference:",c1.circumference())