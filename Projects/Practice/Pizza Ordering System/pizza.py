# Pizza Ordering System

MENU = {
    "margherita": {
        "ingredients": {
            "dough": 1,
            "tomato_sauce": 2,
            "cheese": 2,
        },
        "cost": 8.99,
    },
    "pepperoni": {
        "ingredients": {
            "dough": 1,
            "tomato_sauce": 2,
            "cheese": 2,
            "pepperoni": 1,
        },
        "cost": 10.99,
    },
    "vegetarian": {
        "ingredients": {
            "dough": 1,
            "tomato_sauce": 2,
            "cheese": 2,
            "vegetables": 3,
        },
        "cost": 9.99,
    }
}

profit = 0

inventory = {
    "dough": 5,
    "tomato_sauce": 10,
    "cheese": 10,
    "pepperoni": 5,
    "vegetables": 8,
}

ordering_system_online = True

def process_payment() -> float:
    # TODO: Implement a payment system (you can simplify or expand on the coin system)
    pass

def check_inventory() -> bool:
    # TODO: Check if there are enough ingredients to make the pizza
    pass

def update_inventory():
    # TODO: Update the inventory after making a pizza
    pass

def make_pizza():
    # TODO: Make the pizza and print a success message
    pass

def print_report():
    # TODO: Print the current inventory and profit
    pass

def add_custom_pizza():
    # TODO: Allow the user to create a custom pizza with available ingredients
    pass

def order_pizza():
    pass

def exit_application():
    global ordering_system_online
    ordering_system_online = False


MENU_OPTIONS = [{
    "title": "Order Pizza",
    "action": order_pizza,
    "input": 1,
}, {
    "title": "Create Custom",
    "action": add_custom_pizza,
    "input": 2,
}, {
    "title": "Check Inventory",
    "action": check_inventory,
    "input": 3,
}, {
    "title": "Print Reports",
    "action": print_report,
    "input": 4,
}, {
    "title": "Quit Application",
    "action": exit_application,
    "input": 5,
}]

print("SumoSoft Pizza Ordering System")

# TODO: Implement the main loop for the pizza ordering system
# Include options for ordering pizzas, printing report, adding custom pizzas, and exiting

while ordering_system_online:

    # print the menu options
    for menu_item in MENU_OPTIONS:
        print(f"{menu_item["input"]}.) {menu_item["title"]}")

    while True:
        try:
            user_choice = int(input("Please make a selection: "))
            result = [item for item in MENU_OPTIONS if item["input"] == user_choice][0]
            result["action"]()

            if ordering_system_online == False:
                break

        except ValueError:
            print("This system only accepts numerical entries.")
        except IndexError:
            print(f"Please enter a numerical value 1-{len(MENU_OPTIONS)}.")


print("The pizza ordering system is now closed.")
