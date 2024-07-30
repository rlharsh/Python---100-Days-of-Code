# and operator
variable_a = True
variable_b = True

if variable_a and variable_b:  # True, or false depending upon the passed variables
  print("Truthy")
else:
  print("Falsey")

# or operator
variable_a = False
variable_b = True

if variable_a or variable_b:  # True, or false depending upon the passed variables
  print("Truthy")
else:
  print("Falsey")

# not opeartor
variable_a = 20

if not variable_a > 15:  # True, or false depending upon the passed variable
  print("Truthy")
else:
  print("Falsey")
