import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("🎯 I am thinking of a number between 1 and 99... Can you guess it?")

    attempts = 0  # Count the number of guesses
    
    while True:
        try:
            # Get user input and ensure it's within range
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 99:
                print("⚠ Please enter a number between 1 and 99.")
                continue

            attempts += 1  # Increment the guess count

            # Check if the guess is correct
            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congrats! The number was {secret_number}. You guessed it in {attempts} attempts!")
                break  # Exit loop on correct guess

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
