class Student:
#     def __init__(self,name,standerd,roll_no):
#         self.name = name
#         self.standerd = standerd
#         self.roll_no = roll_no

#     def exam(self,physics,mathematics,chemistry,biology,english):
#         self.physics = physics
#         self.mathematics = mathematics
#         self.chemistry = chemistry
#         self.biology = biology
#         self.english = english
#         return self.physics + self.mathematics + self.chemistry + self.biology + self.english / sum([self.biology, self.english, self.chemistry, self.mathematics, self.physics]) * 100

    
#     def result(self):
#         if self.exam() >= 40:
#             return f"{self.name} has passed the exam with {self.exam()}%."
#         else:
#             return f"{self.name} has failed the exam with {self.exam()}%."
        


# s1 = Student("Mubarak", "10th", 12345)
# s1.exam(85, 90, 78, 88, 92)
# s1.result()