# Type Checking
#
# age = int(input("Enter your age: "))  # Convert to an integer
# print(type(age))  # Print out the DataType: <class 'int'>
#
# age = input("Enter your age: ")  # Accept default of string
# print(type(age))  # Print out the DataType: <class 'str'>

# Type Conversion
#
# age = "28"
# print(2 + int(age))  # Converts the age to an integer type to be consumed
#
# num_char = len(age)  # Convert the length of age to an integer, with len (length)
# print(str(num_char))  # Convert the num_char integer to a string type
a = 123
print(type(a))  # Integer

a = float(a)
print(type(a))  # Float

print(70 + float("100.5"))  # 170.5
