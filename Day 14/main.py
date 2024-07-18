from art import logo, vs
from game_data import data
import random
from os import system, name

# Print 'logo' from art.py
# Pick random 'name', 'description', 'country' and 'follower_count', and print it (except 'folower count')
# Print 'VS' art from art.py
# Pick random 'name', 'description', 'country' and 'follower_count', and print it (except 'folower count')
# Ask for user input to chose either 'A' or 'B'
# Compare user choice to both follower_counts, if user chose one with higher count, then continue game, else print game_over msg
# IF user wins replace correct answer as #1 and generate new random #2
# Continue game WHILE user wins


# Define clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    if is_correct:
        score = +1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
