# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/56feec3f-61a3-47e9-95d9-7f9871a9a09a?sl=d568e30d-6f5e-46d3-9f36-167c874b232a&st=LjVbIcYUBnS3G9xyUt7QmjC6s8Yv8LBI

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    grade = student_scores[key]
    if grade < 70:
        student_grades[key] = "Fail"
        break
    elif grade >= 71 and grade <= 80:
        student_grades[key] = "Acceptable"
    elif grade >= 81 and grade <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif grade >= 91 and grade <= 100:
        student_grades[key] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)
