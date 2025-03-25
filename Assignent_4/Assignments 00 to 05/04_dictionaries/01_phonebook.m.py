def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Enter a contact name (or press Enter to finish): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name} is already in the phonebook with number {phonebook[name]}.")
            continue
        number = input(f"Enter {name}'s phone number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    if not phonebook:
        print("The phonebook is empty.")
    else:
        print("\nPhonebook:")
        for name, number in phonebook.items():
            print(f"{name} -> {number}")
        print()


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter a name to look up (or press Enter to exit): ")
        if name == "":
            print("Exiting lookup mode.")
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s phone number is {phonebook[name]}.")


def main():
    """
    Main function to run the phonebook program.
    """
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    print("Goodbye! Thank you for using the phonebook.")



if __name__ == '__main__':
    main()
