import random

# List of words to guess
word_list = ["python", "hangman", "computer", "programming", "developer", "challenge", "software", "game"]

def choose_word():
    # Randomly select a word from the word_list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Create a display of the word, replacing unguessed letters with '_'
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()  # Random word to guess
    guessed_letters = []  # List of guessed letters
    attempts = 6  # Number of incorrect guesses allowed
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while attempts > 0:
        # Display current progress
        print(display_word(word, guessed_letters))
        print(f"You have {attempts} attempts remaining.")
        
        # Get user's guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # Add guessed letter to the list
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Oops! {guess} is not in the word.")
        
        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
        
    if attempts == 0:
        print(f"Game Over! The word was: {word}")

def main():
    hangman()

if __name__ == '__main__':
    main()
