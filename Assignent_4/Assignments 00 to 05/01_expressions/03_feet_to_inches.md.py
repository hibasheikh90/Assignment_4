"""
Program: feet_to_inches_converter
---------------------------------
This program converts a given length in feet to inches.

Conversion formula:
1 foot = 12 inches

The user inputs a value in feet, and the program outputs the equivalent length in inches.
"""

# Define the conversion factor as a constant
INCHES_IN_FOOT: int = 12

def convert_feet_to_inches(feet: float) -> float:
    """
    Converts feet to inches.
    :param feet: Length in feet
    :return: Equivalent length in inches
    """
    return feet * INCHES_IN_FOOT

def main():
    """
    Prompts the user to enter a value in feet and converts it to inches.
    """
    # Get input from the user
    feet: float = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches: float = convert_feet_to_inches(feet)

    # Display the result
    print(f"{feet} feet is equal to {inches} inches!")

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
