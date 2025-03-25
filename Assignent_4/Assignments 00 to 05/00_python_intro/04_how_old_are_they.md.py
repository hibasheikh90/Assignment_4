def main():
    # Assigning ages based on given conditions
    anton: int = 21  # Anton's age is given as 21 years old
    beth: int = anton + 6  # Beth is 6 years older than Anton
    chen: int = beth + 20  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew's age is Chen's age + Anton's age
    ethan: int = chen  # Ethan's age is the same as Chen's age

    # Printing the ages in the correct format
    print(f"Anton is {anton} years old.")
    print(f"Beth is {beth} years old.")
    print(f"Chen is {chen} years old.")
    print(f"Drew is {drew} years old.")
    print(f"Ethan is {ethan} years old.")

# Ensuring the script runs only when executed directly
if __name__ == '__main__':
    main()