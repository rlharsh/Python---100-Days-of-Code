# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/40e95268-2b4a-4b56-9dee-3df9e198213e?sl=f492fa95-de31-4f7f-ad16-62aef0a47d2b&st=YCckCNG1xhIk3qxZfa4NBuRPddqG5ure
# for number in range(1, 101):
#     if number % 3 == 0:
#         if number % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
