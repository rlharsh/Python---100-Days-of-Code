# Purposeful error
# fruits = ["Apple", "Oranges", "Pineapple"]
# print(fruits[len(fruits)])

# Correct
# fruits = ["Apple", "Oranges", "Pineapple"]
# print(fruits[len(fruits) - 1])

# Dirty Dozens
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#                "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
