import math
# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e242258e-5006-40f1-9228-8e3a8c7482cc?sl=0d712e20-d561-45cf-bfbf-c92981083867&st=z0IFbiDuWJfMR7kz7qBfuQgxDzjqkjal
# Write your code below this line 👇
def paint_calc(height, width, cover):
    total_paint_needed = math.ceil((height * width) / cover)
    print(f"You'll need {total_paint_needed} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
