def get_input(word_type):
    return input(f"Please enter a {word_type}: ")

def programming_mad_libs():
    # Get user input for various parts of speech
    verb1 = get_input("verb (e.g., run, debug, compile)")
    noun1 = get_input("noun (e.g., bug, keyboard, code)")
    adjective1 = get_input("adjective (e.g., funny, complicated, fast)")
    verb2 = get_input("verb (e.g., crash, compile, execute)")
    noun2 = get_input("noun (e.g., function, loop, error)")
    adjective2 = get_input("adjective (e.g., confusing, slow, brilliant)")
    
    # Template for the Mad Libs story
    story = f"Once upon a time, a programmer decided to {verb1} the {noun1}. It was {adjective1}, but the code kept trying to {verb2}. The {noun2} was so {adjective2} that it took forever to fix!"
    
    # Print the resulting story
    print("\nHere's your funny programming story:\n")
    print(story)

def main():
    print("Welcome to the Mad Libs Programming Edition!")
    programming_mad_libs()

if __name__ == '__main__':
    main()
