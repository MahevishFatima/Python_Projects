# Python code to play 21 Number game with hints

import sys

# returns the nearest multiple to 4
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def show_correct_strategy():
    print("\n--- WINNING STRATEGY ---")
    print("To win the 21 game, you must always stop at these numbers:")
    print("4, 8, 12, 16, 20")
    print("If you do this, the computer will be forced to say 21.")
    print("-------------------------")

def lose1():
    print("\n\nYOU LOSE !")
    print("Better luck next time !")
    show_correct_strategy()
    sys.exit(0)

# checks whether the numbers are consecutive
def check(xyz):
    for i in range(1, len(xyz)):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
    return True

# starts the game
def start1():
    xyz = []
    last = 0

    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ').strip().upper()

        # player takes the first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("How many numbers do you wish to enter? (1-3)")
                    try:
                        inp = int(input('> '))
                    except ValueError:
                        print("Invalid input. You are disqualified!")
                        lose1()

                    if inp < 1 or inp > 3:
                        print("Wrong input. You are disqualified!")
                        lose1()

                    comp = 4 - inp
                    print("Now enter the values:")

                    temp = []
                    for _ in range(inp):
                        try:
                            a = int(input('> '))
                        except ValueError:
                            print("Invalid input. You are disqualified!")
                            lose1()
                        temp.append(a)

                    # check consecutiveness with previous sequence
                    if not xyz:
                        if temp[0] != 1:
                            print("You must start with 1.")
                            lose1()

                    xyz.extend(temp)
                    last = xyz[-1]

                    if not check(xyz):
                        print("\nYou did not input consecutive integers.")
                        lose1()

                    if last == 21:
                        lose1()

                    # Computer's turn
                    for j in range(1, comp + 1):
                        xyz.append(last + j)
                    print("Order of inputs after computer's turn is:")
                    print(xyz)
                    last = xyz[-1]

        # player takes the second chance
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                # Computer's turn
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Order of inputs after computer's turn is:")
                print(xyz)

                if xyz[-1] == 20:
                    lose1()

                print("\nYour turn.")
                print("How many numbers do you wish to enter? (1-3)")
                try:
                    inp = int(input('> '))
                except ValueError:
                    print("Invalid input. You are disqualified!")
                    lose1()

                if inp < 1 or inp > 3:
                    print("Wrong input. You are disqualified!")
                    lose1()

                temp = []
                print("Enter your values:")
                for _ in range(inp):
                    try:
                        val = int(input('> '))
                    except ValueError:
                        print("Invalid input. You are disqualified!")
                        lose1()
                    temp.append(val)

                xyz.extend(temp)
                last = xyz[-1]

                if not check(xyz):
                    print("\nYou did not input consecutive integers.")
                    lose1()

                near = nearestMultiple(last)
                comp = near - last
                if comp == 4:
                    comp = 3

            print("\n\nCONGRATULATIONS !!!")
            print("YOU WON !")
            sys.exit(0)

        else:
            print("Wrong choice, try again.")

# Main loop
game = True
while game:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ').strip().lower()
    if ans == 'yes':
        start1()
    elif ans == 'no':
        print("Do you want to quit the game? (yes / no)")
        nex = input('> ').strip().lower()
        if nex == "yes":
            print("You are quitting the game...")
            sys.exit(0)
        elif nex == "no":
            print("Continuing...")
        else:
            print("Wrong choice")
    else:
        print("Wrong choice, enter Yes or No.")



""""
Player 2 is Computer.
Do you want to play the 21 number game? (Yes / No)
> yes
Enter 'F' to take the first chance.
Enter 'S' to take the second chance.
> F

Your Turn.
How many numbers do you wish to enter? (1-3)
> 3
Now enter the values
> 1
> 2
> 3
Order of inputs after computer's turn is:
[1, 2, 3, 4]
""""
