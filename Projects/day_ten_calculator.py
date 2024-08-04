from calculator_art import logo as art

# add
def add(n1, n2) -> int:
    """
    add Adds to numbers together.

    Args:
        n1 (int): The first number to be added
        n2 (int): The second number to be added

    Returns:
        int: The value of n1 + n2
    """
    return n1 + n1


# subtract
def subtract(n1, n2) -> int:
    """
    subtract Subtracts to value of n2 from n1.

    Args:
        n1 (int): The number to be subracted from
        n2 (int): The number to be subtracted

    Returns:
        int: The value of n1 - n2
    """
    return n1 - n2


# multiply
def multiply(n1, n2) -> int:
    """
    multiply Multiplies two numbers

    Args:
        n1 (int): The first number to be multiplied
        n2 (int): The second number to be multiplied

    Returns:
        int: The value of n1 * n2
    """
    return n1 * n2


# divide
def divide(n1, n2) -> int:
    """
    divide Divides the value of n1 by the value of n2

    Args:
        n1 (int): The first number to be divided
        n2 (int): The second number to be divided

    Returns:
        int: The value of n1 / n2.
    """
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

number_one = int(input("What's the first number?: "))
for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")
number_two = int(input("What's the second number?: "))

print(f"{number_one} {operation_symbol} {number_two} = {operations[operation_symbol](number_one, number_two)}")
