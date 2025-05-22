# I'm just learn


# It's better to create a password yourself because it's easy to remember
#Version 1 , not use randomize and etc.
#manual with formula + seed . U can edit the formula to get different passowrd. Thanks 

import string

def generate_password(length, seed):
    if length < 8 or length > 64:
        print("Password length must be between 8 and 64 characters.")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lowercase + uppercase + digits + symbols

    password = ""
    for i in range(length):
        char = all_chars[(i * 11 + length * 5 + ord(seed[i % len(seed)])) % len(all_chars)]
        password += char

    return password

def main():
    try:
        length = int(input("Enter password length (8-64): "))
        seed = input("Enter a seed (your name, word, anything): ")
        password = generate_password(length, seed)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
