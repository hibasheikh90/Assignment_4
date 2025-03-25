def double(num: int):
    """
    This function takes a number and returns it multiplied by 2.
    """
    return num * 2


def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
