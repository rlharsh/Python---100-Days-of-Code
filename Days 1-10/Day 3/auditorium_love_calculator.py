# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/6bd4bb59-cd10-4657-b677-a79a6f03f44b?sl=3232881b-77b4-4179-b219-1ebca53fbb09&st=o5bSZ3jIbWAHysFhKE3t59IiQY4M0jLS
#
# Description:

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1.lower() + name2.lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
first_digit = t + r + u + e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')
second_digit = l + o + v + e

final_score = int(str(first_digit) + str(second_digit))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
else:
    if final_score >= 40 and final_score <= 50:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}.")
