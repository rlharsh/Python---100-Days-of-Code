numbers = [74, 86, 88, 71, 96, 98, 100, 77, 84, 88, 95]

print(sum(numbers))                             ## Sum
print(round(sum(numbers) / len(numbers), 2))    ## Average

name_list = ["Ronald", "Peggy", "Sumo", "Peggy", "Idgi"]
print(set(name_list))                           ## Set removes duplicate entries

list_one = ["Cat", "Chicken", "Dog"]
list_two = ["Horse", "Pig", "Duck"]
list_one.sort()
list_two.sort()
list_three = list_one + list_two
list_three.sort()
print(list_three)
