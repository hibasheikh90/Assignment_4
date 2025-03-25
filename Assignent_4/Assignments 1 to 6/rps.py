import random

def play_rps():
    # Options for Rock, Paper, and Scissors
    choices = ["rock", "paper", "scissors"]
    
    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Check if the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return
    
    # Computer randomly chooses
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_rps()

if __name__ == '__main__':
    main()
