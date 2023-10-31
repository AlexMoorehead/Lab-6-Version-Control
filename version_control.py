# Prints menu options to user
def print_menu():
    print('Menu')
    print('-' * 13)
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
    usable_list = []
    for element in password:
        item = int(element) - 3
        usable_list.append(item)
        # decided to modify Alex's logic since it seemed more conscise then mine
        n = 0
        for item in usable_list:
           if item == -1:
               usable_list[n] = 9
           if item == -2:
               usable_list[n] = 8
           # deals with the negative numbers
           if item == -3:
               usable_list[n] = 7
           n += 1
    n = 0
    for element in usable_list:
        usable_list[n] = str(usable_list[n])
        n += 1
    decoded = "".join(usable_list)
    return decoded

# Main program loop, takes menu inputs and calls respective methods.
while True:
    print_menu()
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        orig_pass = input("Please enter your password to encode: ")
        encoded_pass = encode(orig_pass)
        print("Your password has been encoded and stored!\n")

    elif menu_input == 2:
        encode = encode(orig_pass)
        decoded = decode(encode)
       # uses the actual programs that are written
        print(f"The encoded password is {encode}, and the original password is {decoded}.")
        pass

    elif menu_input == 3:
        break

    else:
        print("Error: Invalid user input.")
