import random
import string

def generate_password(length):
    # Define the characters to be included in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    try:
        # Get the password length from the user
        length = int(input("Enter the desired length of your password: "))
        
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
        else:
            password = generate_password(length)
            print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == '__main__':
    main()
