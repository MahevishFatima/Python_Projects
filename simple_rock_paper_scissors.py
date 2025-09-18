import random

# Print multiline instruction
print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

while True:
    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors")

    # Take the input from user safely
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number (1/2/3).")
        continue

    # Validate choice
    if choice not in choices:
        print("Invalid choice! Please select between 1, 2, or 3.")
        continue

    # User choice
    user_choice = choices[choice]
    print("User choice is:", user_choice)

    # Computer choice
    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice]
    print("Computer choice is:", comp_choice_name)

    print(user_choice, "vs", comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")
