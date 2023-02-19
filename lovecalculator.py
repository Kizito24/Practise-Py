# Don't change code below this line
print("Welcome to the love calculator!")
name1 = input("what is your name?")
name2 = input("What is their name?")
# Don't change code above this line

# Write code below this line
combined_name = name2 + name1
case_string = combined_name.lower()

t = case_string.count("t")
r = case_string.count("r")
u = case_string.count("u")
e = case_string.count("e")

true = t + r + u + e

l = case_string.count("l")
o = case_string.count("o")
v = case_string.count("v")
e = case_string.count("e")

love = l + o + v + e

love_score = int(str(true + love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")
