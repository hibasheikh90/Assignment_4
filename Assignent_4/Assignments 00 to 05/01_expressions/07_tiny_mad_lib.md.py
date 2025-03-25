# Define the sentence starter
SENTENCE_START: str = "Code in Place is fun. I learned to program and used Python to make my "  

def main():
    """
    This function prompts the user for an adjective, a noun, and a verb,
    then constructs and prints a fun sentence using those words.
    """
    # Ask the user for an adjective
    adjective: str = input("Please type an adjective and press enter: ")  

    # Ask the user for a noun
    noun: str = input("Please type a noun and press enter: ")  

    # Ask the user for a verb
    verb: str = input("Please type a verb and press enter: ")  

    # Construct and display the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")  

# Required to call the main function when the script runs
if __name__ == '__main__':
    main()
