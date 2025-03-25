MAX_LENGTH : int = 3  # Maximum allowed length of the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Last element remove karna
        print("Removed:", removed_item)  # Removed item print karna

########## No need to edit code past this point ##########

def main():
    my_list = []
    
    # User se list ki values lena
    while True:
        value = input("Enter a value (or press enter to stop): ")
        if value == "":
            break  # Jab user khali enter press kare to stop
        my_list.append(value)  # List me value add karne ke liye

    print("List before:", my_list)
    shorten(my_list)  # shorten function call karne ke liye
    print("List after:", my_list)  # Final list print karne ke liye

if __name__ == "__main__":
    main()
