# Don't change the code below
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
mape = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Put spaces between the digit ")
# Don't change the code above

vpsition = int(position[0])
hpsition = int(position[1])

mape[vpsition - 1][hpsition - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
