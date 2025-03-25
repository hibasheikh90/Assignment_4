from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Checks if the provided password (after hashing) matches the stored hashed password.

    Parameters:
    - email (str): The email associated with the stored password.
    - stored_logins (dict): Dictionary mapping emails to their hashed passwords.
    - password_to_check (str): The password input that needs to be validated.

    Returns:
    - True if the email exists and the password matches.
    - False otherwise.
    """
    return stored_logins.get(email) == hash_password(password_to_check)

def hash_password(password):
    """
    Converts a password into a secure SHA256 hash.

    Parameters:
    - password (str): The plain text password.

    Returns:
    - (str): The hashed version of the password.
    """
    return sha256(password.encode()).hexdigest()

def main():
    # Dictionary storing email-password pairs (hashed)
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    # Test cases
    print(login("example@gmail.com", stored_logins, "word"))        # False
    print(login("example@gmail.com", stored_logins, "password"))    # True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False
    print(login("student@stanford.edu", stored_logins, "password")) # False
    print(login("student@stanford.edu", stored_logins, "123!456?789")) # True
    print(login("unknown@email.com", stored_logins, "password"))    # False (email not found)

if __name__ == '__main__':
    main()
