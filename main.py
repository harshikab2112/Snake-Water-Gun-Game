"""
snake: -1
water: 0
gun: 1
"""

"""
Snake vs. Water → Snake wins (Snake drinks the water)
Water vs. Gun → Water wins (Water rusts the gun)
Gun vs. Snake → Gun wins (Gun shoots the snake)
"""

import random

print(" 'Snake, Water, Gun Game' ")
print("\nChoice: 's' for Snake, 'w' for Water, 'g' for Gun\n")
computer = random.choice([-1, 0, 1])
user = input("Enter your choice: ")
user_dict = {
    "s": -1,
    "w": 0,
    "g": 1,
}
user_value = user_dict[user]

reverse_dict = {-1: "Snake", 0: "Water", 1: "Gun"}

print(
    f"You chose: {reverse_dict[user_value]}\nComputer chose: {reverse_dict[computer]}"
)

if computer == user_value:
    print("DRAW !!!\n")
else:
    if (computer == -1) and (user_value == 0):
        print("You Lose!!\n")
    elif (computer == 0) and (user_value == 1):
        print("You Lose!!\n")
    elif (computer == 1) and (user_value == -1):
        print("You Lose!!\n")
    elif (computer == 0) and (user_value == -1):
        print("You Win!!\n")
    elif (computer == 1) and (user_value == 0):
        print("You Win!!\n")
    elif (computer == -1) and (user_value == 1):
        print("You Win!!\n")
    else:
        print("Something went wrong\n")
