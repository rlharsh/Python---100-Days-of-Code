# URL:
#
# Description:
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Input
# L
# Y
# N
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

final_price = 0
if size == "S":
    final_price += 15
elif size == "M":
    final_price += 20
elif size == "L":
    final_price += 25

if add_pepperoni == "Y":
    if size == "S":
        final_price += 2
    else:
        final_price += 3

if extra_cheese == "Y":
    final_price += 1

if final_price > 0:
    print(f"Your final bill is: ${final_price}.")
