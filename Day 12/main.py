# Number Guessing Game Objectives:
# from curses.ascii import isdigit
from art import logo, game_over
import random
from os import system, name


# Function to clear screen
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def difficulty():
    while True:
        diff_choice = (
            input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        )

        if diff_choice in ["easy", "hard"]:
            break
        else:
            print("Invalid input. Please enter 'easy' or 'hard'!")

    if diff_choice == "easy":
        x = 10
    elif diff_choice == "hard":
        x = 5
    else:
        x = "Invalid input. Please enter 'easy' or 'hard'!"

    return int(x)


def game():
    random_number = random.randint(1, 100)

    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print(f"Pssst, the correct answer is {random_number}")

    num_of_attempts = difficulty()
    print(f"You have {num_of_attempts} attempts remaining to guess the number.")

    while True:
        user_guess = input("Make a guess: ")

        if user_guess.isdigit() and 0 < int(user_guess) < 100:
            user_guess = int(user_guess)
            num_of_attempts -= 1

            if user_guess < random_number:
                print("Your guess is too low. Try again.")
                print(
                    f"You have {num_of_attempts} attempts remaining to guess the number."
                )
            elif user_guess > random_number:
                print("Your guess is too high. Try again.")
                print(
                    f"You have {num_of_attempts} attempts remaining to guess the number."
                )
            else:
                print(
                    f"Congratulations! You guessed the correct number {random_number}."
                )
                break
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

        if num_of_attempts == 0:
            clear()
            print(game_over)
            print("You've run out of guesses. Game Over")
            break


game()
