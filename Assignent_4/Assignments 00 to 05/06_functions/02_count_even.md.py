def count_even(lst):
    """
    This function counts the number of even numbers in the provided list `lst`.
    """
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print("Number of even numbers:", even_count)


def populate_list():
    """
    This function prompts the user to enter integers until they press enter without typing anything.
    It then returns the list of integers entered.
    """
    user_list = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop when the user presses enter without entering a number
        try:
            num = int(user_input)  # Convert input to an integer
            user_list.append(num)  # Add the number to the list
        except ValueError:
            print("Please enter a valid integer.")
    
    return user_list


def main():
    user_list = populate_list()  # Populate the list with user input
    count_even(user_list)  # Count and print the even numbers in the list


if __name__ == "__main__":
    main()
