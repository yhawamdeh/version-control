def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    password = ""
    for digit in encoded_password:
        new_digit = (int(digit) - 3) % 10
        password += str(new_digit)
    return password

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("\nPlease enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!\n")

    elif choice == "2":
        if not encoded_password:
            print("No password has been encoded yet.\n")
        else:
            print("The encoded password is", encoded_password, "and the original password is", decode(encoded_password) + ".\n")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")