def main():
    # Prompt the user to enter a number and convert it to float
    num: float = float(input("Type a number to see its square: "))

    # Calculate the square of the number
    square = num ** 2

    # Print the result using f-string for better readability
    print(f"{num} squared is {square}")

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
