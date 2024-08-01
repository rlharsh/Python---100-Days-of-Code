# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/3c6091ed-ef4e-4247-82ae-167a2cb5208f?sl=1ea8e61d-4da3-4d1b-9c45-aed9ac32a221&st=Lkstz5KiPP91iISobr9xtB8AeKba3EVt
#
# INSTRUCTIONS:
# Write a program that calculates the
# Body Mass Index (BMI) from a user's weight and height.

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_feet = float(height)
weight_pounds = float(weight)

height_inches = height_feet * 12
user_bmi = (weight_pounds / (height_inches ** 2)) * 703

user_bmi = round(user_bmi, 2)
print(f"Your BMI is {user_bmi:.2f}")
