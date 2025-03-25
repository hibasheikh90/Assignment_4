def guess_the_number():
    # Set the range for the guess
    lower_bound = 1
    upper_bound = 100
    attempts = 0
    
    print(f"Welcome to 'Guess the Number' game!")
    print(f"Please think of a number between {lower_bound} and {upper_bound} and I will try to guess it.")
    input("Press Enter when you're ready...")

    while True:
        # Computer makes a guess
        guess = (lower_bound + upper_bound) // 2  # Guess the middle number
        attempts += 1

        # Ask the user if the guess is correct, too high, or too low
        print(f"My guess is: {guess}")
        user_feedback = input("Is this guess too high (H), too low (L), or correct (C)? ").lower()

        # Check the user's feedback and adjust the range
        if user_feedback == 'c':
            print(f"Yay! I guessed your number {guess} correctly in {attempts} attempts!")
            break
        elif user_feedback == 'h':
            upper_bound = guess - 1
        elif user_feedback == 'l':
            lower_bound = guess + 1
        else:
            print("Invalid input! Please enter 'H', 'L', or 'C'.")

def main():
    guess_the_number()

if __name__ == '__main__':
    main()
