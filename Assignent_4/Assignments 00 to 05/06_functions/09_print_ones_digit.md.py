def print_ones_digit(num: int):
    """
    This function takes an integer num and prints its ones digit.
    """
    ones_digit = num % 10  # The ones digit is the remainder when divided by 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    print_ones_digit(num)  # Call the function to print the ones digit


if __name__ == '__main__':
    main()
