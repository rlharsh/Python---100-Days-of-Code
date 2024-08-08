# understanding scope
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside of function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
#print(potion_strength)

# global scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# scope
# game_level = 2
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# create_enemy()

# modify global scope
# enemies = "Skeleton"

# def increase_enemies():
#     global enemies
#     enemies = "Zombie"
#     print(f"Enemies inside of the function: {enemies}")

# increase_enemies()
# print(f"Enemies outside the function: {enemies}")

# a more sound solution to modifying global scoped variables
# enemies = 1

# def inscrease_enemies(enemy: int) -> int:
#     print(f"Enemies inside function: {enemies}.")
#     return enemy + 1

# enemies = inscrease_enemies(enemy=enemies)
# print(f"Enemies outside function: {enemies}.")

# constants
# PI = 3.14159

# def calc():
#     print(PI)

# calc()
def a_function(a_parameter):
    a_variable = 15
    return a_parameter

a_function(10)
print(a_variable)
