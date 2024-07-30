# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/7a12b4b1-76d3-4d04-820d-938547daba55?sl=eb333545-4ecd-4273-bee6-62561b17c787&st=9HOXX6cF3RnnbdAcCm5XJ5PNq704Z9Mb
#
# Instructions:
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

user_height = input("What is your height?: ")
user_weight = input("What is your weight?: ")

height_feet = float(user_height)
weight_pounds = float(user_weight)

height_inches = height_feet * 12
user_bmi = (weight_pounds / (height_inches ** 2)) * 703

user_bmi = round(user_bmi, 2)

if user_bmi < 35:
    if user_bmi <= 18.5:
        print("You are underweight")
    elif user_bmi <= 25:
        print("You are a normal weight.")
    elif user_bmi <= 30:
        print("You are slightly overweight.")
    elif user_bmi <= 35:
        print("You are obese.")
elif user_bmi >= 35:
    print("You are clinically obese.")
