def main():
    my_list = []
    
    while True:
        value = input("Enter a value: ")
        if value == "":  # Agar user sirf enter press kare
            break  # Loop se bahar aa jy ga
        my_list.append(value)  # List me value add kane ke liye
    
    print("Here's the list:", my_list)  # Final list print karne ke liye

if __name__ == "__main__":
    main()
