def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each element doubled.

    :param numbers: A list of integers.
    :return: A new list where each number is doubled.
    """
    doubled_list = [num * 2 for num in numbers]  # Using list comprehension to double each number
    return doubled_list


def main():
    numbers = [1, 2, 3, 4]  # Define the original list
    doubled_numbers = double_numbers(numbers)  # Call function to get the doubled list
    print("Original list:", numbers)
    print("Doubled list:", doubled_numbers)  # Print the new doubled list


if __name__ == "__main__":
    main()
