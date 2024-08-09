# broken code
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
##      The for loop is looping over numbers from 1-19

# 2. When is the function meant to print "You got it"?
##      "You got it" should be printed when i is equal to 20

# 3. What are your assumptions about the value of i?
##      The value of i never reaches 20, it reaches 19

# fixed code from above
# def my_function_fixed():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")

# my_function_fixed()

# reproduce bug
# from random import randint
# dice_images = ["😁", "😂", "😍", "😭", "😘", "🤔"]
# dice_num = randint(0, 5)  ## adjust randint(1, 6) to randint(0, 5)
# print(dice_images[dice_num])

# try/except
# try:
#     age = int(input("How old are you? "))
#     if age > 18:
#         print(f"You can drive a care at {age}.")
# except ValueError:
#     print("Unexpected input.")

# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)

# Debugger
# import random
# import math

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = math.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

# def even_or_odd(number) -> str:
#     return "Your number is even!" if number % 2 == 0 else "Your number is odd!"

# print(even_or_odd(13))
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap(2000))

# Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)

# fizz_buzz(15)
