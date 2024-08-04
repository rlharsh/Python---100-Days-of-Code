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

def get_number(prompt):
    """
    get_number Asks the user for an integer input and returns the value.

    Args:
        prompt (string): The prompt to be displayed

    Returns:
        int: The integer conversion of given input string
    """
    return int(input(prompt))

def get_operation():
    """
    get_operation Verifies and returns the mathematical operation

    Returns:
        string: The verified mathematical operation
    """
    while True:
        print(" ".join(operations.keys()))
        operation = input("Pick an operation from the line above: ")
        if operation in operations:
            return operation
        print("Invalid operation. Please try again.")


def calculate(current_result=None):
    """
    calculate The core loop of the application that calculates 2 numbers.

    Args:
        current_result (int, optional): The overall results of conversion. Defaults to None.

    Returns:
        int: The results of the calculation
    """
    if current_result is None:
        current_result = get_number("What's the first number: ")

    while True:
        operation = get_operation()
        next_number = get_number("What's the next number?: ")
        current_result = operations[operation](current_result, next_number)
        print(f"{current_result} {operation} {next_number} = {current_result}")

        continue_calc = input(f"Type 'y' to continue calculating with {current_result}, or type 'n' to exit: ").lower()
        if continue_calc != 'y':
            break

    return current_result

results = calculate()
print(f"Final result: {results}")
