import random

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


lp_index = str(0)
lp = ""
for i in range(1, nr_letters):
    lp_index = random.randint(0, len(letters))
    lp += letters[lp_index]
print(lp)

sp_index = str(0)
sp = ""
for n in range(1, nr_symbols):
    sp_index = random.randint(0, len(symbols))
    sp += symbols[sp_index]
print(sp)

np_index = str(0)
np = ""
for x in range(1, nr_numbers):
    np_index = random.randint(0, len(numbers))
    np += numbers[np_index]
print(np)

password = np + sp + lp
print(f"Your Easy level password is {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
