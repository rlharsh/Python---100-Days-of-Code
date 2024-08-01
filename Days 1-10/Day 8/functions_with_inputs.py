# basic function
# def greet():
#     print("Hello")
#     print("from")
#     print("greet!")

# greet()

# function with argument
# def example(argument):
#     print(argument)

# example("Testing")

# greeting function with argument
# def greet(name):
#     print(f"Hello {name}!")

# greet("Ronald L. Harsh")

# greeting function with two arguments
# def greet(name, location):
#     """greet _summary_

#     Args:
#         name (name): string: The name of the user
#         location (location): string: The location of the user
#     """
#     print(f"Hello {name}, how is the weather in {location} today?")
# greet(location="Ronald", name="Wausau, WI")

# greeting with keyword arguments
def greet(name, location):
    """greet Prints a greeting message to the user console window

    Args:
        name (string): The name of the user.
        location (string): The location of the user.
    """
    print(f"Hello {name}, how is the weather in {location}?")
greet(location="Wausau, WI", name="Ronald")
