# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/4a109ef8-ac17-4a51-85b1-61a61a20bb66?sl=9f11a807-0fb7-4665-b939-db4e73addf51&st=mNE31MHkIOQ6aD7idTqayqxc4JmqYIyT

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
average_height = 0
number_of_students = 0
total_height = 0

for n in range(0, len(student_heights)):
    total_height += student_heights[n]
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")
