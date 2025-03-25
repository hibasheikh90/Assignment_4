def add_three_copies(my_list, data):
    """Adds three copies of the given data to the list."""
    for _ in range(3):
        my_list.append(data)



def main():
    """Main function to get user input and demonstrate mutability."""
    message = input("Enter a message to copy: ")
    my_list = []
    
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
