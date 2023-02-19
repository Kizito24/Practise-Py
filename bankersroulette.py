import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
r_rol = random.randint(0, num_items - 1)

print(names[r_rol])
