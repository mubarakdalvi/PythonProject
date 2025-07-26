
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
