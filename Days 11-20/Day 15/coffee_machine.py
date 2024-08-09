MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins(drink_price: int) -> int:
    print(f"Your total is ${round(drink_price, 2)}, please insert coins.")
    total = int(input("How many quarters: ")) * .25
    total +=int(input("How many dimes: ")) * .10
    total +=int(input("How many nickles: ")) * .05
    total +=int(input("How many pennies: ")) * .01
    return total


def resources_available(ingredients: dict) -> bool:
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def transaction_success(collected: int, drink_cost: int) -> bool:
    if collected >= drink_cost:
        change_due = round(collected - drink_cost, 2)
        print(f"Here is ${change_due} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you have not given enough money to make drink.")
        return False


def make_coffee(drink_name: str, drink_ingredients: dict):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}, enjoy!")


def print_report():
    global profit
    print(f"Water : {resources['water']}")
    print(f"Milk  : {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profit: {profit}")

is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print_report()
    else:
        drink = MENU[user_choice]
        if resources_available(ingredients=drink["ingredients"]):
            payment = process_coins(drink_price=drink["cost"])
            if transaction_success(collected=payment, drink_cost=drink["cost"]):
                make_coffee(drink_name=user_choice, drink_ingredients=drink["ingredients"])



print("The machine is now off.")
