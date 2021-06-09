import random
import string


def computer(choices):
    return random.choice(choices)


def who_is_winner(user, comp, choices):
    strong = []
    weak = []
    global rating
    if choices.index(user) > len(choices) // 2:
        for x in range(1, len(choices) // 2 + 1):
            strong.append(choices[choices.index(user) - x])
        weak = [x for x in choices if x not in strong]
    else:
        for x in range(1, len(choices) // 2 + 1):
            weak.append(choices[choices.index(user) + x])
        strong = [x for x in choices if x not in weak]

    if user == comp:
        rating += 50
        print_result("draw", comp)
    elif comp in weak:
        print_result("computer", comp)
    elif comp in strong:
        rating += 100
        print_result("user", comp)


def print_result(result, comp):
    if result == "user":
        print(f"Well done. The computer chose {comp} and failed")
    elif result == "computer":
        print(f"Sorry, but the computer chose {comp}")
    else:
        print(f"There is a draw ({comp})")


name = input("Enter your name: ").capitalize()
print(f"Hello, {name}")
game_options = input().split(",")
if len(game_options) < 3:
    game_options = ["rock", "paper", "scissors"]

print("Okay, let's start")
rating_file = open("rating.txt", "r")
name_list = rating_file.readlines()
name_dict = {}
rating = 0

for i in name_list:
    name_dict[i.strip(" \n").strip(string.digits).strip()] \
        = i.strip("\n").strip(string.ascii_letters).strip()

if name in name_dict:
    rating = int(name_dict[name])

rating_file.close()

while True:
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(f"Your rating: {rating}")
    elif user_choice in game_options:
        computer_choice = computer(game_options)
        who_is_winner(user_choice, computer_choice, game_options)
    else:
        print("Invalid input")
