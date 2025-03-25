def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes a list of numbers and returns their sum.

    :param numbers: A list of integers.
    :return: The sum of all numbers in the list.
    """
    total: int = 0  # Initialize the sum variable
    for number in numbers:  
        total += number  # Add each number to the total

    return total  # Return the final sum


def main():
    numbers = [1, 2, 3, 4, 5]  # Define a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Get the sum
    print(f"The sum of the numbers is: {sum_of_numbers}")  # Print the result


if __name__ == "__main__":
    main()

