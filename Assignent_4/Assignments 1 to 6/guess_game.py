import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)  # Random number between 1 and 100
    attempts = 0
    
    print(f"Welcome to 'Guess the Number' game!")
    print(f"Guess the number between {lower_bound} and {upper_bound}!")

    while True:
        # Get user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts!")
            break  # Exit the loop when the correct number is guessed

def main():
    guess_the_number()

if __name__ == '__main__':
    main()
