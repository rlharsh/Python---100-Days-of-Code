user_height = int(input("What is your height?: " ))
ticket_price = 0

if user_height > 120:  # True
    print("You can ride the rollercoaster!")
    user_age = int(input("What is your age?: "))
    if user_age < 12:  # True
        ticket_price = 5
        print("Child tickets are $5.")
    elif user_age <= 18:  # True
        ticket_price = 7
        print("Youth tickets are $7.")
    elif user_age >= 45 and user_age <= 55:
        ticket_price = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:  # False
        ticket_price = 12
        print("Adult tickets are $12.")
    wants_photos = input("Do you want photographs?: ")
    if wants_photos == "yes":  # True
        ticket_price += 3
    print(f"Your ticket price is ${ticket_price}.")
else:  # False
    print("Sorry, you have to grow taller before you can ride.")
