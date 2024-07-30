# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
import random

names = "Angela, Ben, Jenny, Michael, Chloe"

names_array = names.split(", ")
user_who_must_pay = random.randint(0, len(names_array) - 1)

print(f"{names_array[user_who_must_pay]} is going to buy the meal today!")
# 🚨 Remember to remove the print statement above when you submit.
