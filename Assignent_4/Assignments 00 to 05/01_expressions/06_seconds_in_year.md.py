# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365  
HOURS_PER_DAY: int = 24  
MIN_PER_HOUR: int = 60  
SEC_PER_MIN: int = 60  

def main():
    """
    Calculates the total number of seconds in a year 
    using predefined constants and prints the result.
    """
    # Calculate the total number of seconds in a year
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN  

    # Print the result in a user-friendly format
    print(f"There are {seconds_in_year} seconds in a year!")  

# Ensuring the script runs only when executed directly
if __name__ == '__main__':
    main()
