# a = int(25)
# b = str('gd')
# c = float(25.00)
# d = bool(False)
# e = None
# f = complex(2j)
# g = range(20)
# hg = list(str(12))
# i = tuple((24,4))
# j = set((3245,54564))
# k = dict({"name": "Mub"})
# l = frozenset((14,451,5))

# # operators arithematic

# r1 = a * c
# r2 = a + c
# r3 = a - c
# r4 = a / c
# r5 = a % c

# print(r1,r2,r3,r4,r5)

# # operators comparison

# r6 = a == c
# r7 = a >= c
# r8 = a <= c
# r9 = a > c
# r10 = a < c
# r11 = a != c

# print(r6,r7,r8,r9,r10,r11)


# # operators logical

# r12 = a and c
# r13 = a or c 
# r14 = not a and c

# print(r12,r13,r14)

# # operators bitwise

# r15 = a & int(c)
# r16 = a | int(c)
# r17 = a ^ int(c)
# r18 = a << 2
# r19 = a >> 2
# r120 = ~a
# r121 = ~int(c)

# print(r15,r16,r17,r18,r19,r120,r121)

# # operators assignment

# a += 2
# a -= 2
# a *= 2
# a /= 2
# a %= 2


# # operators identity

# r27 = a is c
# r28 = a is not c

# print(r27,r28)


# # operators membership

# r29 = a in g
# r30 = a not in g

# print(r29,r30)

# # operators special

# # r31 = a // c  # Floor division
# # r32 = a ** 2  # Exponentiation

# # print(r31, r32)


# # studentWhoAre18 = [{
# #     "name" : "Mubarak",
# #     "Age" : 10
# # },
# # {    "name" : "Ali","Age" : 17},
# # {    "name" : "Ahmed","Age" : 15},
# # {    "name" : "Sara","Age" : 31},
# # {    "name" : "Hassan","Age" : 21}
# # ]

# # for i in studentWhoAre18:
# #     if i["Age"] >= 18:
# #         print(f"{i['name']} is {i['Age']} years old and is eligible to vote.")
# #     else:
# #         print(f"{i['name']} is {i['Age']} years old and is not eligible to vote.")


# # import random
# # password = random.randint(1000, 9999)
# # print(password)

# # chances = 3

# # while chances:
# #     transaction = input('Enter a numebr: ')
# #     if not transaction.isdigit():
# #         print('Please enter a valid number.')
# #         continue
# #     if transaction == str(password):
# #         print('You guessed the password correctly!')
# #         break
# #     else:
# #         chances -= 1 
# #         if chances > 0:
# #             print(f'Wrong guess! You have {chances} chances left.')
# #         else:
# #             print(f'Sorry, you have used all your chances. The password was {password}.') 



# calculator

# def add(*Args):
#     result = 0
#     for num in Args:
#         result += num
#     return result

# def subtract(*Args):
#     if len(Args) == 0:
#         return 0
#     result = Args[0]
#     for num in Args[1:]:
#         result -= num
#     return result

# def multiply(*Args):
#     result = 1
#     for num in Args:
#         result *= num
#     return result

# def divide(*Args):
#     if len(Args) == 0:
#         return 0
#     result = Args[0]
#     for num in Args[1:]:
#         if num == 0:
#             return "Cannot divide by zero"
#         result /= num
#     return result

# def modulus(*Args):
#     if len(Args) == 0:
#         return 0
#     result = Args[0]
#     for num in Args[1:]:
#         if num == 0:
#             return "Cannot perform modulus with zero"
#         result %= num
#     return result


# def calculator(operation, *args):
#     if operation == 'add':
#         return add(*args)
#     elif operation == 'subtract':
#         return subtract(*args)
#     elif operation == 'multiply':
#         return multiply(*args)
#     elif operation == 'divide':
#         return divide(*args)
#     elif operation == 'modulus':
#         return modulus(*args)
#     else:
#         return "Invalid operation"
    
# Calculator = calculator('subtract', 10, 20, 30, 40)

# print(Calculator)

#list 

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("Original List:", lst)

# # list comprehension to create a new list with squares of even numbers

# sqr = [i**2 for i in lst]

# print(sqr)

# lst[0:7] = "Mubarak"

# print("Modified String:", lst)

# pyramid pattern

# for i in range(1, 7):
#     print(" " * (5 - i) + "*" * i + "*" * (i - 1))

# file = open("new.txt", "w+")
# n = int(input("Enter the number : "))
# for i in range(n):
#     file.write(f"{ " " * (n - i) + "*" * i + "*" * (i - 1)}\n")
# file.close()


# with open("new.txt", "w+") as file:
#     file.write("new")
#     file.seek(0)
#     content = file.read()
#     print(content)

# import os

# to remove the file 
# os.remove("new.txt")

# prac = open("new.txt", "w+")
# prac.write("Hi everyone \ni am learning file i/o\n")
# prac.write("using java\n")
# prac.write("I like programming in java\n")
# prac.seek(0)
# content = prac.read()
# print(content)
# prac.close()

# def changejava():
#     with open("new.txt", "w+") as file:
#         file.write(f"{content.replace('java', 'python')}")
#         file.seek(0)
#         file_content = file.read()
#         print(file_content)
#         file.close()
# changejava()


# def findlearning():
#     with open("new.txt", "r") as file:
#         content = file.read()
#         if "learning" in content:
#             print("The word 'learning' is present in the file.")
#         else:
#             print("The word 'learning' is not present in the file.")
#         file.close()
# findlearning()

# str1 = "Mubarak"
# for i in str1:
#     print(i.upper(),end=" ")



# list1 = sorted([i ** 2 for i in range(1, 11) if i % 2 == 0])
# print(list1)


#exception handling


# def ageGroup():
#     age = None
#     try:
#         age = float(input("Enter ypur age : "))
#         if age == 0:
#             print("You are just born.")
#         if 3 <= age <= 18:
#             if age < 8:
#                 print("You are an infant.")
#             else:
#                 print("You are a child.")
#         elif age > 18  and age <= 50:
#             print("You are an adult.")
#         else:
#             print("You are senior.")
#     except (ValueError, TypeError) as e:
#         print(f"An error occurred: {e}. Please enter a valid age.")
#     finally:
#         year = int(age)
#         month = int((age - year) * 12)
#         days = int((((age - year) * 12) - month) * 30) 
#         if age is not None:
#             print(f"Thank you for using the age group checker, your age is {year} Years and {month} months and {days} days old .")
#         else:
#             print("Thank you for using the age group checker.")
# ageGroup()

#list

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lst[0] = "Mubarak" # mutable, assigning a new value to the first element
# print(lst)

# lst[0:7] = "Mubarak" #slicing 
# print(lst)

# # lst = [i**2 for i in lst] # list comprehension
# # print(lst)

# lst.append(11) 
# print(lst)

# lst.remove(11)
# print(lst)

# lst.pop(0)
# print(lst)

# del lst[0]
# print(lst)

# lst.clear() 
# print(lst)

# set1 = {1, 2, 3, 4, 5}
# print(set1)

# set1.add(6)  # Adding an element
# print(set1)

# set1.remove(6)  # Removing an element
# print(set1)

# set1.discard(5)  # Discarding an element
# print(set1)

# set1.pop()  # Removing an arbitrary element
# print(set1)

# set1.clear()  # Clearing the set
# print(set1)

# set1.copy()
# print(set1)

# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)

# tuple1 = tuple1 + (6,) # Adding an element (tuples are immutable, so we create a new tuple)
# print(tuple1)

# tuple1 = tuple1[:-1]  # Removing the last element (creating a new tuple)
# print(tuple1)

# tuple1 = tuple1[1:]  # Slicing the tuple
# print(tuple1)

# tuple1 = tuple1 + (7, 8, 9)  # Concatenating another tuple
# print(tuple1)

# dict1 = {"name": "Mubarak", "age": 25}

# dict1["city"] = "Lagos"  # Adding a new key-value pair

# dict1["age"] = 26  # Modifying an existing key-value pair
# print(dict1)

# dict1.pop("city")  # Removing a key-value pair

# dict1.clear()  # Clearing the dictionary

# dict1.update({"country": "Nigeria", "language": "English"})  # Updating the dictionary with new key-value pairs

# dict1.values()  # Getting all values from the dictionary
# print(dict1)


#class

# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# p1 = Person("Mubarak", 25)

# class Student(Person):
#     def __init__(self,name,age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def greet(self):
#         super().greet()
#         print(f"My student ID is {self.student_id}.")

# s1 = Student("Ali", 20, "S12345")
# s1.greet()

# class Student:
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
#         total = self.physics + self.mathematics + self.chemistry + self.biology + self.english
#         return total / len([self.biology, self.english, self.chemistry, self.mathematics, self.physics])

    
#     def result(self):
#         percentage = self.exam(self.physics, self.mathematics, self.chemistry, self.biology, self.english)
#         if percentage >= 40:
#             return f"{self.name} has passed the exam with {percentage:.2f}%."
#         else:
#             return f"{self.name} has failed the exam with {percentage:.2f}%."
        
#     @staticmethod # for withtout instantiation, means adding self as paramter. 
#     def hello():
#         return "Hello, I am a student."
    
#     def __cannot_call(self):
#         return "This method cannot be called directly." 



# s1 = Student("Mubarak", "10th", 12345)
# s1.exam(95, 90, 98, 98, 92)
# print(s1.result())
# print(s1.hello())
# print(s1._Student__cannot_call())  # Accessing the private method using name mangling
# print(s1.__cannot_call()) # This will raise an AttributeError since __cannot_call is private and cannot be accessed directly.
