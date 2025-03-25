def main():
    """
    This program takes two integers from the user, performs division, 
    and prints the quotient and remainder.
    """

    # Take input for the two numbers
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulus operator gives remainder

    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Ensuring the script runs only when executed directly
if __name__ == '__main__':
    main()
