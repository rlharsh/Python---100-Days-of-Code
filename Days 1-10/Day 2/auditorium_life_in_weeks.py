# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/70ce34ac-2968-4f2d-a523-964c824f7892?sl=42bdaa61-096d-4f32-8f1c-371f681345f6&st=voOVSS863JuNoRgjspfGFZBADWEmqWar
#
# Description:
# Create a program using maths and f-Strings
# that tells us how many weeks we have left,
# if we live until 90 years old.
#
# It will take your current age as the input
# and output a message with our time left in
# this format:
#
# You have x weeks left.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
print(f"You have {(90 * 52) - (int(age) * 52)} weeks left.")
