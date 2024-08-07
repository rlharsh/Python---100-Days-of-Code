from collections import Counter

name_list = ["Peggy", "Ronald", "Sumo", "Idgi", "Peggy"]

my_index = name_list.index("Ronald")            ## Find index
print(my_index)

d = dict.fromkeys(name_list, 0)
for val in name_list:
    d[val] += 1
print(d)

q = Counter(name_list)
print(dict(q))
