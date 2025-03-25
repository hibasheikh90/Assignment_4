# Planetary Weight Calculator

# Define gravity constants for each planet
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0
}

def main():
    # Get user input
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    planet = input("Enter the name of a planet: ").strip()
    
    # Check if the planet exists in our dictionary
    if planet in GRAVITY_FACTORS:
        planetary_weight = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"Your weight on {planet} would be: {planetary_weight} kg")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
