PROMPT: str = "What do you want? "
JOKE: str = """Here is a joke for you!  
Why do programmers prefer dark mode?  
Because light attracts bugs! 😂"""
SORRY: str = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()  # Get user input correctly

    if user_input == "joke":  # Check for an exact match
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
