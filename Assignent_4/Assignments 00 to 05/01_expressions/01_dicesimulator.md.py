"""
Program: dicesimulator
----------------------
Simulate rolling two dice three times and print
the results. This program demonstrates how variable
scope works in Python.
"""

# Import the random library to generate random numbers
import random

# Define the number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice, calculates their total,
    and prints the result.
    """
    die1: int = random.randint(1, NUM_SIDES)  # Generates a random number between 1 and NUM_SIDES
    die2: int = random.randint(1, NUM_SIDES)  # Generates another random number for the second die
    total: int = die1 + die2  # Sum of both dice
    print(f"Total of two dice: {total}")  # Print the total

def main():
    """
    Demonstrates local and global variable scope while
    simulating dice rolls.
    """
    die1: int = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")  # Prints the initial value of die1 in main()

    # Call roll_dice() three times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() is: {die1}")  # Prints die1 in main() again to show it hasn’t changed

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
