import math  # Importing math module to use sqrt function

def main():
    """
    This program calculates the hypotenuse (BC) of a right triangle 
    using the Pythagorean theorem: BC² = AB² + AC²
    """
    
    # Take input for two perpendicular sides and convert them to float
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Print the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Ensuring the script runs only when executed directly
if __name__ == '__main__':
    main()
