def list_practice():
    # Problem #1: List Practice
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print(f"The length of the fruit list is: {len(fruit_list)}")
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "List updated successfully!"
    return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end] if 0 <= start < len(lst) and 0 <= end <= len(lst) else "Invalid range."

def index_game():
    # Problem #2: Index Game
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    while True:
        print("\nList Operations:")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Exit")
        choice = input("Choose an operation (1-4): ")
        
        if choice == '1':
            idx = int(input("Enter index to access: "))
            print("Element at index", idx, ":", access_element(my_list, idx))
        
        elif choice == '2':
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, idx, new_val))
            print("Updated list:", my_list)
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    list_practice()
    index_game()
