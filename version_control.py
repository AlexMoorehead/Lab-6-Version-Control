# Prints menu options to user
def print_menu():
    print('Menu')
    print('-' * 12)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')


# Takes in user password and shifts each digit up by 3 numbers, looping over 9 if needed.
def encode(password):
    pass_list = []
    for char in password:
        new_digit = (int(char) + 3) % 10
        pass_list.append(str(new_digit))
    return ''.join(pass_list)


# Takes in encoded user password and shifts each digit down by 3 numbers.
def decode(password):
    pass


# Main program loop, takes menu inputs and calls respective methods.
while True:
    print_menu()
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        orig_pass = input("Please enter your password to encode: ")
        encoded_pass = encode(orig_pass)
        print("Your password has been encoded and stored!\n")

    elif menu_input == 2:
        print('')
        pass

    elif menu_input == 3:
        break

    else:
        print("Error: Invalid user input.")