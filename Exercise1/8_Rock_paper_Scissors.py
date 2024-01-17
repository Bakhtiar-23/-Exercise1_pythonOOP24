import random

# Function to get the user's choice
def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win this round!"
    else:
        return "Computer wins this round!"

# Function to play the Rock-Paper-Scissors game
def play_game():
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_wins += 1
        elif "Computer wins" in result:
            computer_wins += 1

        print(f"Score - You: {user_wins}, Computer: {computer_wins}\n")

    if user_wins == 3:
        print("Congratulations! You won the game.")
    else:
        print("Sorry! Computer won the game.")

# Play the game
play_game()
