# Simple example
# def return_two():
#     return 2
# my_variable = return_two()
# print(str(my_variable))

# Functions with Outputs
# def format_name(first_name, last_name):
#     return(f"{first_name.title()} {last_name.title()}")

# print(format_name("ronald", "harsh"))

# Returning multiple Outputs
def format_name(first_name, last_name):
    # check if values were passed
    if first_name == "" or last_name == "":
        return "Unknown User"  # escape the function

    formatted_f_name = first_name.title()
    formatted_l_name = last_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))
