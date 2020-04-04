import os
import sys

def starting_number_sticks():
    while True:
            try:
                sticks = int(input("How many sticks do you want to start with (10-100)? "))
            except ValueError:
                print("That's not a number!\n")
            else:
                if 10 <= sticks <= 100:
                    return sticks
                else:
                    print("Need a number between 10 and 100!\n")

def user_picks_sticks():
    while True:
        try:
            num_sticks = int(input("How many sticks do you pick up (1-3)? "))
        except ValueError:
            print("That's not a number!\n")
        else:
            if 1 <= num_sticks <= 3:
                return num_sticks
            else:
                print("Need a number between 1 and 3!\n")


def determine_turn(number_of_turns):
    if number_of_turns % 2 == 1:
        #Player 1
        return True
    elif number_of_turns % 2 == 0:
        #Player 2
        return False


def play_again():
    """Asks user if they want to play the game again."""

    play_again = input("Do you want to play Mystery Word again? [y/N] \n")

    if play_again.lower().strip() == "y":
        clear()
        main()

    else:
        print("Thank you. We appreciate your business.")
        sys.exit()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    total_number_sticks = 0
    number_of_turns = 1

    print ("Welcome to the Game of Sticks!")

    total_number_sticks = starting_number_sticks()

    while total_number_sticks > 0:

        clear()
        print("\nThere are {} sticks on the board.\n".format(total_number_sticks))

        if determine_turn(number_of_turns):
            print("\nPlayer 1's turn:\n")
            total_number_sticks -= user_picks_sticks()
        else:
            print("\nPlayer 2's turn:\n")
            total_number_sticks -= user_picks_sticks()
        number_of_turns +=1

    else:
        if determine_turn(number_of_turns):
            print("\nPlayer 1 wins!\n")
        else:
            print("\nPlayer 2 wins!\n")

        play_again()

if __name__ == '__main__':
    main()
