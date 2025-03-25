"""
Program: mass_energy_converter
------------------------------
This program continuously reads mass (kg) from the user and calculates
the equivalent energy using Einstein's mass-energy equivalence formula:

E = m * c^2

where:
- E = Energy in joules
- m = Mass in kilograms (user input)
- C = Speed of light (constant: 299792458 m/s)

The program runs in a loop until the user enters a negative mass or zero.
"""

# Define the speed of light in meters per second (constant)
C: int = 299792458

def calculate_energy(mass: float) -> float:
    """
    Calculates energy using Einstein's formula: E = m * C^2
    :param mass: Mass in kilograms
    :return: Equivalent energy in joules
    """
    return mass * (C ** 2)

def main():
    """
    Continuously prompts the user for mass and calculates the corresponding energy.
    Stops when the user enters zero or a negative number.
    """
    while True:
        # Get mass input from user
        mass_in_kg: float = float(input("Enter kilos of mass (or 0 to exit): "))

        # Exit condition
        if mass_in_kg <= 0:
            print("Exiting program. Thank you!")
            break

        # Calculate energy
        energy_in_joules = calculate_energy(mass_in_kg)

        # Display calculation steps and result
        print("\ne = m * C^2...")
        print(f"m = {mass_in_kg} kg")
        print(f"C = {C} m/s")
        print(f"{energy_in_joules:.2e} joules of energy!\n")  # Display energy in scientific notation

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()