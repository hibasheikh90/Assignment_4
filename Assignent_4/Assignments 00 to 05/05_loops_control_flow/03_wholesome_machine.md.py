AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    
    while True:
        user_feedback = input()  # Get user's input
        if user_feedback == AFFIRMATION:
            print("That's right! :)")
            break  # Exit the loop when the correct affirmation is entered
        else:
            print("That was not the affirmation. Please try again!")
            print("Please type the following affirmation: " + AFFIRMATION)

if __name__ == '__main__':
    main()
