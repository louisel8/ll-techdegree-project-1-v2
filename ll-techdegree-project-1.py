"""
Python Development Techdegree
Project 1 (V3) - The Number Guessing Game
--------------------------------
"""

import random

print('''

Hey friend, welcome to the number guessing game.
During the game, you can continuously guess the number with the prompt notice.
Until the correct number be guessed. Good luck!

    ''')

def start_game(previous_number=None):
    if previous_number is None:
        the_number = random.randint(1, 10)
        #print(the_number)
        count_guess = 0
    else:
        the_number = previous_number
        count_guess = 0

    while True:
        try:
            guessed_number = int(input("Please guess an integer number between 1 to 10: "))
            if guessed_number < 1 or guessed_number > 10:
                raise ValueError("Guessed number is outside the range.")

            count_guess += 1
            if guessed_number < the_number:
                print("The correct number is bigger, please try bigger numbers.")
            elif guessed_number > the_number:
                print("The correct number is smaller, please try smaller numbers.")
            else:
                print(
                    f"You got it! The number is {the_number}; it took {count_guess} attempt(s) to guess correctly this time.")
                print("")
                return count_guess, the_number
        except ValueError as e:
            print(f"Error: {e}")
            while True:
                option = input("A. Resume game; B. Start over; C. Exit: ").lower()
                if option not in ["a", "b", "c"]:
                    print("Invalid option. Please choose A, B or C.")
                else:
                    break

            if option == "a":
                print("Resuming the round...")
                continue


            elif option == "b":
                the_number = random.randint(1, 10)
                #print(the_number)
                count_guess = 0
                print("Starting over the game.")
                continue

            elif option == "c":
                return None, None
                print("Exiting the game...")

def play_game():
    least_temp = []
    round = 1
    count_guess = 0
    the_number = None

    while True:
        print(f"=> Let's start round {round}")
        if the_number is None:
            count_guess, the_number = start_game(the_number)
            if count_guess is None or the_number is None:
                print("Exiting the game...")
                break
            least_temp.append(count_guess)
        else:
            count_guess, the_number = start_game(the_number)
            if count_guess is None or the_number is None:
                print("Exiting the game...")
                break
            least_temp.append(count_guess)

        if count_guess is not None and the_number is not None:
            while True:
                try:
                    option = input("A. Start new round; B. Exit; ").lower()
                    if option not in ["a", "b"]:
                        raise ValueError('Invalid option. Please enter "A" to start a new round or "B" to exit the game.')
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            if option == "b":
                print("Your best score is {}-attempt(s).".format(min(least_temp)))
                print("You have now exited the game! Goodbye & Have a great day!")
                break

            elif option == "a":
                the_number = random.randint(1, 10)
                round = round + 1
                #print(the_number)
                continue


        print("")

play_game()
