def main():
    curr_value = int(input("Enter a number: "))  # Get user's input

    while curr_value < 100:  # Continue doubling until curr_value reaches 100 or more
        curr_value *= 2
        print(curr_value)  # Print the doubled value

# Run the main function
if __name__ == "__main__":
    main()
