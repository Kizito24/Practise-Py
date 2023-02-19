import random
user_choice = int(input("What do you choose? Type 0 for Rock 1 for Paper and 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

print(f"{computer_choice}")


if user_choice == 0 and computer_choice == 2:
    print("You wins")
elif user_choice == 2 and computer_choice == 0:
    print("You loose")
elif computer_choice > user_choice:
    print("You loose")
elif computer_choice < user_choice < 2:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice > 2:
    print("You typed an invalid number.\nYou loose")
else:
    print("You typed an invalid number.\nYou loose")
