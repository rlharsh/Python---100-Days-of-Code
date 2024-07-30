# nested if statement
# user_height = int(input("What is your height?: "))

# if user_height > 120:  # True
#     user_age = int(input("What is your age?: "))
#     if user_age > 18:  # True
#         print("Your fee is $12 to ride this ride.")
#     else:  # False
#         print("Your fee is $7 to ride this ride.")
# else:  # False
#     print("I am sorry, you cannot ride this ride.")

# if / elif / else
user_height = int(input("What is your height?: " ))

if user_height > 120:  # True
    print("You can ride the rollercoaster!")
    user_age = int(input("What is your age?: "))
    if user_age < 12:  # True
        print("Please pay $5.")
    elif user_age <= 18:  # True
        print("Please pay $7.")
    else:  # False
        print("Please pay $12.")
else:  # False
    print("Sorry, you have to grow taller before you can ride.");
